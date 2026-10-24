# C++ API

`slideio::openSlide()` opens a slide and returns an object of class
`slideio::Slide`. That class exposes methods for the slide's properties,
including its metadata and associated images. A single `slideio::Slide` can
hold several raster images, each represented by a `slideio::Scene`. For example,
a CZI file can contain several scanned regions, each of them a separate scene.
`slideio::Scene` exposes the methods for reading raster data and per-scene
metadata.

`slideio::getDriverIDs()` lists the IDs of the available
[image drivers](../drivers.md). Pass one of them to `openSlide()` to force a
driver, or leave the driver empty to let the library detect the format.

The API uses only standard C++ types, so a program that includes SlideIO does
not need OpenCV on its include path.

## Example

Read the central quarter of the first scene of a slide:

```cpp
std::shared_ptr<slideio::Slide> slide = slideio::openSlide(path, "GDAL");
const int numScenes = slide->getNumScenes();
if(numScenes>0) {
    std::shared_ptr<slideio::Scene> scene = slide->getScene(0);
    const std::tuple<int, int, int, int> sceneRect = scene->getRect();
    const int sceneWidth = std::get<2>(sceneRect);
    const int sceneHeight = std::get<3>(sceneRect);
    const int blockWidth = sceneWidth / 2;
    const int blockHeight = sceneHeight / 2;
    const int blockOriginX = sceneWidth / 4;
    const int blockOriginY = sceneHeight / 4;
    std::tuple<int, int, int, int> blockRect(blockOriginX, blockOriginY, blockWidth, blockHeight);
    const std::tuple<int, int> blockSize(blockWidth, blockHeight);
    const int numChannels = scene->getNumChannels();
    const int memSize = scene->getBlockSize(blockSize, 0, numChannels, 1, 1);
    std::vector<uint8_t> rasterData(memSize);
    scene->readBlock(blockRect, rasterData.data(), rasterData.size());
}
```

## Reference

The [C++ API reference](reference/index.md) documents every public header,
grouped by module.
