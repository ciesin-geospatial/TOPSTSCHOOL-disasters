import rasterio
import numpy as np
import matplotlib.pyplot as plt

def calculate_ndwi(green_path, nir_path, output_path=None, show_plot=True):
    """
    Calculate NDWI from Landsat 8 bands and save/plot the result.
    green_path: path to Band 3 (Green) GeoTIFF
    nir_path: path to Band 5 (NIR) GeoTIFF
    output_path: (optional) path to save NDWI GeoTIFF
    show_plot: (default True) display NDWI map
    """
    # Open the Green and NIR band files
    with rasterio.open(green_path) as green_src, rasterio.open(nir_path) as nir_src:
        green = green_src.read(1).astype('float32')
        nir = nir_src.read(1).astype('float32')
        profile = green_src.profile

    # Avoid division by zero
    np.seterr(divide='ignore', invalid='ignore')
    ndwi = (green - nir) / (green + nir)
    ndwi = np.nan_to_num(ndwi, nan=0.0, posinf=0.0, neginf=0.0)

    # Save NDWI as GeoTIFF if output_path is provided
    if output_path:
        profile.update(dtype=rasterio.float32, count=1)
        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(ndwi, 1)

    # Plot NDWI
    if show_plot:
        plt.figure(figsize=(8,6))
        plt.imshow(ndwi, cmap='Blues', vmin=-1, vmax=1)
        plt.colorbar(label='NDWI')
        plt.title('Normalized Difference Water Index (NDWI)')
        plt.axis('off')
        plt.show()

    return ndwi

# Example usage:
# calculate_ndwi('LC08_L1TP_XXX_B3.TIF', 'LC08_L1TP_XXX_B5.TIF', output_path='ndwi.tif')