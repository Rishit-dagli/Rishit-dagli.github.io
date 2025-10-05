#!/bin/bash

# Configuration - Edit these settings
QUALITY="high"  # "high" or "low"

# List of classes and their corresponding output image names
# Format: "ClassName:output-file-name"
CLASSES=(
    "SpringMassSystem:spring-mass-system"
    "SpringMassSystemDark:spring-mass-system"
    "TangentCovectorSpace:tangent-covector-space"
    "TangentCovectorSpaceDark:tangent-covector-space"
    "CylindricalCrossProduct:cylindrical-cross-product"
    "CylindricalCrossProductDark:cylindrical-cross-product"
    "SkewSymmetricMatrix:skew-symmetric-matrix"
    "SkewSymmetricMatrixDark:skew-symmetric-matrix"
    "HamiltonianVectorField:hamiltonian-vector-field"
    "HamiltonianVectorFieldDark:hamiltonian-vector-field"
    "CotangentBundleVisualization:cotangent-bundle-visualization"
    "CotangentBundleVisualizationDark:cotangent-bundle-visualization"
    "DegreeOneFlow:degree-one-flow"
    "DegreeOneFlowDark:degree-one-flow"
    "CosphereBundle:cosphere-bundle"
    "CosphereBundleDark:cosphere-bundle"
    "EnergyLevelCircle:energy-level-circle"
    "EnergyLevelCircleDark:energy-level-circle"
    "GeodesicComparison:geodesic-comparison"
    "GeodesicComparisonDark:geodesic-comparison"
    "LightCone:light-cone"
    "LightConeDark:light-cone"
    # Add more classes here as needed
)

# Set quality flag for manim
if [ "$QUALITY" = "high" ] || [ "$QUALITY" = "h" ]; then
    QUALITY_FLAG="-qh"  # Removed -p flag to prevent auto-preview
    echo "Running in HIGH quality mode"
elif [ "$QUALITY" = "low" ] || [ "$QUALITY" = "l" ]; then
    QUALITY_FLAG="-ql"  # Removed -p flag to prevent auto-preview
    echo "Running in LOW quality mode"
else
    echo "Invalid quality. Use 'high' or 'low'"
    exit 1
fi

# Clean up any existing media folder
if [ -d "media" ]; then
    echo "Cleaning up existing media folder..."
    rm -rf media
fi

# Create assets directory if it doesn't exist
ASSETS_DIR="../../assets/diff-geometry"
mkdir -p "$ASSETS_DIR"

echo "Processing ${#CLASSES[@]} classes..."

# Process each class
for class_config in "${CLASSES[@]}"; do
    # Split class name and image name
    IFS=':' read -r CLASS_NAME IMAGE_NAME <<< "$class_config"
    
    # Determine theme suffix based on class name
    THEME_SUFFIX=""
    if [[ "$CLASS_NAME" == *"Dark"* ]]; then
        THEME_SUFFIX="-dark"
    else
        THEME_SUFFIX="-light"
    fi
    
    echo ""
    echo "=== Processing: $CLASS_NAME ==="
    echo "Output image will be named: ${IMAGE_NAME}${THEME_SUFFIX}"
    
    # Run manim command
    manim $QUALITY_FLAG diff-geometry.py $CLASS_NAME
    
    if [ $? -ne 0 ]; then
        echo "Manim execution failed for $CLASS_NAME!"
        continue
    fi
    
    # Find the generated image file
    MEDIA_DIR="media/images/diff-geometry"
    if [ ! -d "$MEDIA_DIR" ]; then
        echo "Media directory not found: $MEDIA_DIR"
        continue
    fi
    
    # Find the most recent PNG file in the media directory
    GENERATED_IMAGE=$(find "$MEDIA_DIR" -name "*.png" -type f -printf '%T@ %p\n' | sort -n | tail -1 | cut -d' ' -f2-)
    
    if [ -z "$GENERATED_IMAGE" ]; then
        echo "No PNG image found in $MEDIA_DIR for $CLASS_NAME"
        continue
    fi
    
    echo "Found generated image: $GENERATED_IMAGE"
    
    # Copy the image to assets folder with the theme suffix
    cp "$GENERATED_IMAGE" "$ASSETS_DIR/${IMAGE_NAME}${THEME_SUFFIX}.png"
    
    if [ $? -eq 0 ]; then
        echo "Successfully copied image to: $ASSETS_DIR/${IMAGE_NAME}${THEME_SUFFIX}.png"
    else
        echo "Failed to copy image to assets folder for $CLASS_NAME"
        continue
    fi
    
    echo "$CLASS_NAME processed successfully!"
done

# Clean up media folder
echo ""
echo "Cleaning up media folder..."
rm -rf media

echo ""
echo "All classes processed successfully!"
echo "Images saved in: $ASSETS_DIR/"
echo "Light theme images: *-light.png"
echo "Dark theme images: *-dark.png"
