#!/bin/bash
# Convert DWG to DXF using ODA File Converter in Docker
#
# Prerequisites:
#   1. Docker must be running
#   2. Download ODA File Converter Linux .deb from:
#      https://www.opendesign.com/guestfiles/oda_file_converter
#   3. Place the .deb file in this directory (next to Dockerfile.oda)
#
# Usage:
#   ./convert_dwg_oda.sh [input.dwg] [output.dxf]

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INPUT_FILE="${1:-$SCRIPT_DIR/2F_C戶- 雲川- 建築水電圖115.03.02.dwg}"
OUTPUT_FILE="${2:-$SCRIPT_DIR/floorplan_oda.dxf}"

IMAGE_NAME="oda-converter"

# Check Docker
if ! docker info > /dev/null 2>&1; then
    echo "ERROR: Docker is not running. Please start Docker Desktop first."
    exit 1
fi

# Check input file
if [ ! -f "$INPUT_FILE" ]; then
    echo "ERROR: Input file not found: $INPUT_FILE"
    exit 1
fi

INPUT_DIR="$(cd "$(dirname "$INPUT_FILE")" && pwd)"
INPUT_BASENAME="$(basename "$INPUT_FILE")"
OUTPUT_BASENAME="$(basename "$OUTPUT_FILE")"

# Build image if not exists
if ! docker image inspect "$IMAGE_NAME" > /dev/null 2>&1; then
    echo "Building ODA File Converter Docker image..."
    echo "Make sure you have the ODA .deb file in: $SCRIPT_DIR"

    # Check for the .deb file
    DEB_COUNT=$(ls "$SCRIPT_DIR"/ODAFileConverter_QT6_lnx_*.deb 2>/dev/null | wc -l)
    if [ "$DEB_COUNT" -eq 0 ]; then
        echo ""
        echo "ERROR: ODA File Converter .deb package not found!"
        echo "Please download it from:"
        echo "  https://www.opendesign.com/guestfiles/oda_file_converter"
        echo "Choose: Linux - .deb (QT6)"
        echo "Place the downloaded .deb file in: $SCRIPT_DIR"
        exit 1
    fi

    docker build -f "$SCRIPT_DIR/Dockerfile.oda" -t "$IMAGE_NAME" "$SCRIPT_DIR"
fi

# Create temp directories for input and output (to isolate the single file)
TMPDIR=$(mktemp -d)
OUTDIR=$(mktemp -d)
trap "rm -rf $TMPDIR $OUTDIR" EXIT

# Copy input file to temp dir
cp "$INPUT_FILE" "$TMPDIR/"

echo "Converting: $INPUT_BASENAME -> $OUTPUT_BASENAME"
echo "Using ODA File Converter in Docker..."

# Run conversion
# Args: input_dir output_dir output_version output_format recursive audit filter
docker run --rm \
    -v "$TMPDIR:/data/input:ro" \
    -v "$OUTDIR:/data/output" \
    "$IMAGE_NAME" \
    "/data/input" "/data/output" "ACAD2018" "DXF" "0" "1" "*.dwg"

# Find the output file (ODA keeps original name but changes extension)
DXF_FILE=$(find "$OUTDIR" -name "*.dxf" -type f | head -1)

if [ -z "$DXF_FILE" ]; then
    echo "ERROR: Conversion failed - no DXF file produced."
    echo "Check if ODA File Converter is properly installed in the Docker image."
    exit 1
fi

# Copy output to desired location
cp "$DXF_FILE" "$OUTPUT_FILE"
echo "SUCCESS: Output saved to: $OUTPUT_FILE"
echo "File size: $(ls -lh "$OUTPUT_FILE" | awk '{print $5}')"
