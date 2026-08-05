# createImagePacker

## createImagePacker

```TypeScript
function createImagePacker(): ImagePacker
```

Creates an ImagePacker instance. Images occupy a large amount of memory. When you finish using an ImagePacker instance, call [release]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-image-function createImagePacker(): ImagePacker--><!--Device-image-function createImagePacker(): ImagePacker-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | ImagePacker instance created. |

**Example**

```TypeScript
async function CreateImagePacker() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
}
```

