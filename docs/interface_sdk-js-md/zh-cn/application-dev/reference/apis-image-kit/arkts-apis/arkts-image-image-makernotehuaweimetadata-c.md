# MakerNoteHuaweiMetadata

MakerNoteHuaweiMetadata implements Metadata来自Huawei相机的照片元数据。

**继承/实现关系：** MakerNoteHuaweiMetadata implements [Metadata](arkts-image-image-metadata-i.md)

**起始版本：** 23

<!--Device-image-class MakerNoteHuaweiMetadata--><!--Device-image-class MakerNoteHuaweiMetadata-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## 导入模块

```TypeScript
import { image } from '@kit.ImageKit';
```

## clone

```TypeScript
clone(): Promise<MakerNoteHuaweiMetadata>
```

对[MakerNoteHuaweiMetadata](#makernotehuaweimetadata)元数据进行克隆。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-clone(): Promise<MakerNoteHuaweiMetadata>--><!--Device-MakerNoteHuaweiMetadata-clone(): Promise<MakerNoteHuaweiMetadata>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[MakerNoteHuaweiMetadata](arkts-image-image-makernotehuaweimetadata-c.md)&gt; | Promise对象，当成功获取元数据时返回MakerNoteHuaweiMetadata元数据实例。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Clone(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // 图片包含exif metadata。
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
  let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
  if (metaData != null) {
    let new_metadata: image.Metadata = await metaData.clone();
    new_metadata.getProperties(["ImageWidth"]).then((data1) => {
      console.info(`Clone new_metadata and get Properties: ${data1}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to clone new_metadata, error : ${err}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function CloneFunc(metadata: image.Metadata): void {
  try {
    let newMetadata = await metadata.clone();
    console.info(0x00000, 'CloneFunc', 'clone success!');
  } catch (err) {
    console.error(0x00000, 'CloneFunc', 'CloneFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataClone(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    let new_metadata = await metaData.exifMetadata.clone();
    new_metadata.getProperties(["ImageWidth"]).then((data1) => {
      console.info(`Succeeded in cloning metadata and getting properties. Data: ${JSON.stringify(data1)}.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to clone metadata and get properties. Code: ${err.code}, message: ${err.message}.`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function exifMetadataClone(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    try {
      const exif = metaData?.exifMetadata;
      if (exif) {
        let new_metadata = await exif.clone();
        let data = new_metadata.getProperties(["ImageWidth"]);
        const count = Object.keys(data).length;
        console.info(`Clone new_metadata and get Properties: ${data}`);
      }
    } catch ( err ) {
      console.error(`Clone new_metadata failed, error : ${err}`);
    }
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function makerNoteHuaweiClone(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    let new_metadata = await metaData.makerNoteHuaweiMetadata.clone();
    new_metadata.getProperties(["HwMnoteIsXmageSupported"]).then((data1) => {
      console.info(`Succeeded in cloning metadata and getting properties. Data: ${JSON.stringify(data1)}.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to clone metadata and get properties. Code: ${err.code}, message: ${err.message}.`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function makerNoteHuaweiMetadataClone(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    try {
      const exif = metaData?.makerNoteHuaweiMetadata;
      if (exif) {
        let new_metadata = await exif.clone();
        let data = new_metadata.getProperties(["HwMnoteIsXmageSupported"]);
        const count = Object.keys(data).length;
        console.info(`Clone new_metadata and get Properties: ${data}`);
      }
    } catch ( err ) {
      console.error(`Clone new_metadata failed, error : ${err}`);
    }
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function heifsMetadataClone(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    let new_metadata = await metaData.heifsMetadata.clone();
    new_metadata.getProperties(["HeifsDelayTime"]).then((data1) => {
      console.info(`Succeeded in cloning metadata and getting properties. Data: ${JSON.stringify(data1)}.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to clone metadata and get properties. Code: ${err.code}, message: ${err.message}.`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function heifsMetadataClone(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    try {
      const exif = metaData?.heifsMetadata;
      if (exif) {
        let new_metadata = await exif.clone();
        let data = new_metadata.getProperties(["HeifsDelayTime"]);
        const count = Object.keys(data).length;
        console.info(`Clone new_metadata and get Properties: ${data}`);
      }
    } catch ( err ) {
      console.error(`Clone new_metadata failed, error : ${err}`);
    }
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function clone(pixelMap: image.PixelMap) {
  pixelMap.clone().then((clonedPixelMap: image.PixelMap) => {
    console.info('Succeeded in cloning the PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to clone the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

ArkTS-Sta示例：

```TypeScript
function clone(pixelMap: image.PixelMap) {
  pixelMap.clone().then((clonedPixelMap: image.PixelMap) => {
    console.info('Succeeded in cloning the PixelMap.');
  }).catch((err: Error) => {
    console.error(`Failed to clone the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```

## createInstance

```TypeScript
static createInstance(): MakerNoteHuaweiMetadata
```

返回[MakerNoteHuaweiMetadata](#makernotehuaweimetadata)的空实例。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-static createInstance(): MakerNoteHuaweiMetadata--><!--Device-MakerNoteHuaweiMetadata-static createInstance(): MakerNoteHuaweiMetadata-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MakerNoteHuaweiMetadata](arkts-image-image-makernotehuaweimetadata-c.md) | 返回MakerNoteHuaweiMetadata的空实例。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
async function exifMetadataCreateInstance(context: Context) {
  let exifMetadata = image.ExifMetadata.createInstance();
  if (exifMetadata != undefined) {
    console.info("Succeeded in creating an ExifMetadata instance.");
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';

async function exifMetadataCreateInstance(context: common.UIAbilityContext) {
  let exifMetadata = image.ExifMetadata.createInstance();
  if (exifMetadata != undefined) {
    console.info("createInstance success");
  }
}
```

ArkTS-Dyn示例：

```TypeScript
async function makerNoteHuaweiCreateInstance(context: Context) {
  let makerNoteHuaweiMetadata = image.MakerNoteHuaweiMetadata.createInstance();
  if (makerNoteHuaweiMetadata != undefined) {
    console.info("Succeeded in creating a MakerNoteHuaweiMetadata instance.");
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';

async function makerNoteHuaweiMetadataCreateInstance(context: common.UIAbilityContext) {
  let makerNoteHuaweiMetadata = image.MakerNoteHuaweiMetadata.createInstance();
  if (makerNoteHuaweiMetadata != undefined) {
    console.info("createInstance success");
  }
}
```

ArkTS-Dyn示例：

```TypeScript
async function heifsMetadataCreateInstance(context: Context) {
  let heifsMetadata = image.HeifsMetadata.createInstance();
  if (heifsMetadata != undefined) {
    console.info("Succeeded in creating a HeifsMetadata instance.");
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { common } from '@kit.AbilityKit';

async function heifsMetadataCreateInstance(context: common.UIAbilityContext) {
  let heifsMetadata = image.HeifsMetadata.createInstance();
  if (heifsMetadata != undefined) {
    console.info("createInstance success");
  }
}
```

## getAllProperties

```TypeScript
getAllProperties(): Promise<Record<string, string | null>>
```

获取图片中所有元数据的属性和值。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-getAllProperties(): Promise<Record<string, string | null>>--><!--Device-MakerNoteHuaweiMetadata-getAllProperties(): Promise<Record<string, string | null>>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Record&lt;string, string \| null&gt;&gt; | Promise对象，返回元数据中定义的所有键值对。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetAllProperties(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // 图片包含exif metadata。
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
  let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
  if (metaData != null) {
    await metaData.getAllProperties().then((data2) => {
      const count = Object.keys(data2).length;
      console.info('Metadata have ', count, ' properties');
      console.info(`Get metadata all properties: ${data2}`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to get metadata all properties. error.code is ${error.code}, error.message is ${error.message}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
function GetAllPropertiesFunc(metadata: image.Metadata): void {
  try {
    let properties = await metadata.getAllProperties();
    console.info(0x00000, 'GetAllPropertiesFunc', 'getAllProperties success!');
  } catch (err) {
    console.error(0x00000, 'GetAllPropertiesFunc', 'GetAllPropertiesFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataGetAllProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    await metaData.exifMetadata.getAllProperties().then((data) => {
      const count = Object.keys(data).length;
      console.info(`Succeeded in getting all properties. Count: ${count}, data: ${JSON.stringify(data)}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to get all properties. Code: ${error.code}, message: ${error.message}.`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function exifMetadataGetAllProperties(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    try {
      const exif = metaData?.exifMetadata;
      if (exif) {
        let data = exif.getAllProperties();
        const count = Object.keys(data).length;
        console.info('Metadata have ', count, ' properties');
        console.info(`Get metadata all properties: ${data}`);
      }
    } catch ( err ) {
      console.error(`Get metadata all properties failed error.code is ${err.code}, error.message is ${err.message}`);
    }
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function makerNoteHuaweiGetAllProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    await metaData.makerNoteHuaweiMetadata.getAllProperties().then((data) => {
      const count = Object.keys(data).length;
      console.info(`Succeeded in getting all properties. Count: ${count}, data: ${JSON.stringify(data)}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to get all properties. Code: ${error.code}, message: ${error.message}.`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function makerNoteHuaweiMetadataGetAllProperties(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    try {
      const exif = metaData?.makerNoteHuaweiMetadata;
      if (exif) {
        let data = exif.getAllProperties();
        const count = Object.keys(data).length;
        console.info('Metadata have ', count, ' properties');
        console.info(`Get metadata all properties: ${data}`);
      }
    } catch ( err ) {
      console.error(`Get metadata all properties failed error.code is ${err.code}, error.message is ${err.message}`);
    }
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function heifsMetadataGetAllProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    await metaData.heifsMetadata.getAllProperties().then((data) => {
      const count = Object.keys(data).length;
      console.info(`Succeeded in getting all properties. Count: ${count}, data: ${JSON.stringify(data)}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to get all properties. Code: ${error.code}, message: ${error.message}.`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function exifMetadataGetAllProperties(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    try {
      const exif = metaData?.heifsMetadata;
      if (exif) {
        let data = exif.getAllProperties();
        const count = Object.keys(data).length;
        console.info('Metadata have ', count, ' properties');
        console.info(`Get metadata all properties: ${data}`);
      }
    } catch ( err ) {
      console.error(`Get metadata all properties failed error.code is ${err.code}, error.message is ${err.message}`);
    }
  } else {
    console.error('Metadata is null.');
  }
}
```

## getBlob

```TypeScript
getBlob(): Promise<ArrayBuffer>
```

以二进制数据的形式获取元数据。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-getBlob(): Promise<ArrayBuffer>--><!--Device-MakerNoteHuaweiMetadata-getBlob(): Promise<ArrayBuffer>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回元数据的二进制数据。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function GetBlob(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let pictureObj: image.Picture = await imageSource.createPicture();
  let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
  let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
  if (metaData != null) {
    let blob = await metaData.getBlob();
    if (blob != undefined) {
      console.info("Succeeded in getting blob.");
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function metadataGetBlob(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let picture = await imageSource.createPicture();
  if (picture != undefined) {
    let metadataType = image.MetadataType.EXIF_METADATA;
    let metadata = await picture.getMetadata(metadataType);
    if (metadata != null) {
      let blob = await metadata.getBlob();
      if (blob != undefined) {
        console.info("get blob success");
      }
    }
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataGetBlob(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    let blob = await metaData.exifMetadata.getBlob();
    if (blob != undefined) {
      console.info("Succeeded in getting blob.");
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function exifMetadataGetBlob(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    const exif = metaData?.exifMetadata;
    if (exif) {
      let blob = await exif.getBlob();
      if (blob != undefined) {
        console.info("get blob success");
      }
    }
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function makerNoteHuaweiGetBlob(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    let blob = await metaData.makerNoteHuaweiMetadata.getBlob();
    if (blob != undefined) {
      console.info("Succeeded in getting blob.");
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function makerNoteHuaweiMetadataGetBlob(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    const exif = metaData?.makerNoteHuaweiMetadata;
    if (exif) {
      let blob = await exif.getBlob();
      if (blob != undefined) {
        console.info("get blob success");
      }
    }
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function heifsMetadataGetBlob(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    let blob = await metaData.heifsMetadata.getBlob();
    if (blob != undefined) {
      console.info("Succeeded in getting blob.");
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function heifsMetadataGetBlob(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    const exif = metaData?.heifsMetadata;
    if (exif) {
      let blob = await exif.getBlob();
      if (blob != undefined) {
        console.info("get blob success");
      }
    }
  }
}
```

## getProperties

```TypeScript
getProperties(key: Array<string>): Promise<Record<string, string | null>>
```

获取图像中属性的值。使用Promise异步回调。要查询的属性的具体信息请参考[PropertyKey](arkts-image-image-propertykey-e.md)。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-getProperties(key: Array<string>): Promise<Record<string, string | null>>--><!--Device-MakerNoteHuaweiMetadata-getProperties(key: Array<string>): Promise<Record<string, string | null>>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | Array&lt;string&gt; | 是 | 要获取其值的属性的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Record&lt;string, string \| null&gt;&gt; | Promise对象，返回元数据要获取的属性的值，如获取失败则返回错误码。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7600202](../errorcode-image.md#7600202-不支持的元数据读写) | Unsupported metadata. Possible causes: unsupported metadata type. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetProperties(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // 图片包含exif metadata。
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
  let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
  if (metaData != null) {
    await metaData.getProperties(["ImageWidth", "ImageLength"]).then((data2) => {
      console.info('Get properties ',JSON.stringify(data2));
    }).catch((error: BusinessError) => {
      console.error(`Failed to get properties. error.code is ${error.code}, error.message is ${error.message}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例:

```TypeScript
function GetPropertiesFunc(metadata: image.Metadata): void {
  try {
    let properties: Record<string, string | null> = await metadata.getProperties(["ImageWidth", "ImageLength"]);
    console.info(0x00000, 'GetPropertiesFunc', 'getProperties success!');
  } catch (err) {
    console.error(0x00000, 'GetPropertiesFunc', 'GetPropertiesFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataGetProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    await metaData.exifMetadata.getProperties(["ImageWidth", "ImageLength"]).then((data) => {
      console.info(`Succeeded in getting properties. Data: ${JSON.stringify(data)}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to get properties. Code: ${error.code}, message: ${error.message}.`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function exifMetadataGetProperties(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    try {
      const exif = metaData?.exifMetadata;
      if (exif) {
        let data = exif.getProperties(["ImageWidth", "ImageLength"]);
        console.info('Get properties ',JSON.stringify(data));
      }
    } catch (err) {
      console.error(`Get properties failed error.code is ${err.code}, error.message is ${err.message}`);
    }
  } else {
    console.error('Metadata is null.');
  }
  fileIo.closeSync(fd);
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function makerNoteHuaweiGetProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    await metaData.makerNoteHuaweiMetadata.getProperties(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]).then((data) => {
      console.info(`Succeeded in getting properties. Data: ${JSON.stringify(data)}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to get properties. Code: ${error.code}, message: ${error.message}.`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function makerNoteHuaweiMetadataGetProperties(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    try {
      const exif = metaData?.makerNoteHuaweiMetadata;
      if (exif) {
        let data = exif.getProperties(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
        console.info('Get properties ',JSON.stringify(data));
      }
    } catch (err) {
      console.error(`Get properties failed error.code is ${err.code}, error.message is ${err.message}`);
    }
  } else {
    console.error('Metadata is null.');
  }
  fileIo.closeSync(fd);
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function heifsMetadataGetProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    await metaData.heifsMetadata.getProperties(["HeifsDelayTime"]).then((data) => {
      console.info('Succeeded in getting properties. ',JSON.stringify(data));
    }).catch((error: BusinessError) => {
      console.error(`Failed to get properties. error.code is ${error.code}, error.message is ${error.message}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function heifsMetadataGetProperties(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    try {
      const exif = metaData?.heifsMetadata;
      if (exif) {
        let data = exif.getProperties(["HeifsDelayTime"]);
        console.info('Get properties ',JSON.stringify(data));
      }
    } catch (err) {
      console.error(`Get properties failed error.code is ${err.code}, error.message is ${err.message}`);
    }
  } else {
    console.error('Metadata is null.');
  }
  fs.closeSync(fd);
}
```

## setBlob

```TypeScript
setBlob(blob: ArrayBuffer): Promise<void>
```

使用二进制数据替换当前元数据。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-setBlob(blob: ArrayBuffer): Promise<void>--><!--Device-MakerNoteHuaweiMetadata-setBlob(blob: ArrayBuffer): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blob | ArrayBuffer | 是 | 要替换的二进制数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7600206](../errorcode-image.md#7600206-无效参数) | Invalid parameter. Possible causes: The blob is empty or has a length of 0. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function setBlob(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let pictureObj: image.Picture = await imageSource.createPicture();
  let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
  let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
  if (metaData != null) {
    let blob = await metaData.getBlob();
    if (blob != undefined) {
      console.info("Succeeded in getting blob.");
      metaData.setBlob(blob);
    }
    let new_blob = metaData.getBlob();
    if (new_blob != undefined) {
      console.info("new_blob is not undefined");
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function metadataSetBlob(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let picture = await imageSource.createPicture();
  if (picture != undefined) {
    let metadataType = image.MetadataType.EXIF_METADATA;
    let metadata = await picture.getMetadata(metadataType);
    if (metadata != null) {
      let blob = await metadata.getBlob();
      if (blob != undefined) {
        console.info("get blob success");
        metadata.setBlob(blob);
      }
      let new_blob = metadata.getBlob();
      if (new_blob != undefined) {
        console.info("new_blob is not undefined");
      }
    }
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataSetBlob(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    let blob = await metaData.exifMetadata.getBlob();
    if (blob != undefined) {
      console.info("Succeeded in getting blob.");
      metaData.exifMetadata.setBlob(blob);
    }
    let new_blob = metaData.exifMetadata.getBlob();
    if (new_blob != undefined) {
      console.info("new_blob is not undefined");
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function exifMetadataSetBlob(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    const exif = metaData?.exifMetadata;
    if (exif) {
      let blob = await exif.getBlob();
      if (blob != undefined) {
        console.info("get blob success");
        exif.setBlob(blob);
      }
      let new_blob = exif.getBlob();
      if (new_blob != undefined) {
        console.info("new_blob is not undefined");
      }
    }
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function makerNoteHuaweiSetBlob(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    let blob = await metaData.makerNoteHuaweiMetadata.getBlob();
    if (blob != undefined) {
      console.info("Succeeded in getting blob.");
      metaData.makerNoteHuaweiMetadata.setBlob(blob);
    }
    let new_blob = metaData.makerNoteHuaweiMetadata.getBlob();
    if (new_blob != undefined) {
      console.info("new_blob is not undefined");
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function makerNoteHuaweiMetadataSetBlob(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    const exif = metaData?.makerNoteHuaweiMetadata;
    if (exif) {
      let blob = await exif.getBlob();
      if (blob != undefined) {
        console.info("get blob success");
        exif.setBlob(blob);
      }
      let new_blob = exif.getBlob();
      if (new_blob != undefined) {
        console.info("new_blob is not undefined");
      }
    }
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function heifsMetadataSetBlob(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    let blob = await metaData.heifsMetadata.getBlob();
    if (blob != undefined) {
      console.info("Succeeded in getting blob.");
      metaData.heifsMetadata.setBlob(blob);
    }
    let new_blob = metaData.heifsMetadata.getBlob();
    if (new_blob != undefined) {
      console.info("new_blob is not undefined");
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function heifsMetadataSetBlob(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    const exif = metaData?.heifsMetadata;
    if (exif) {
      let blob = await exif.getBlob();
      if (blob != undefined) {
        console.info("get blob success");
        exif.setBlob(blob);
      }
      let new_blob = exif.getBlob();
      if (new_blob != undefined) {
        console.info("new_blob is not undefined");
      }
    }
  }
}
```

## setProperties

```TypeScript
setProperties(records: Record<string, string | null>): Promise<void>
```

批量设置图片元数据中的指定属性的值。使用Promise异步回调。要查询的属性的具体信息请参考[PropertyKey](arkts-image-image-propertykey-e.md)。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-setProperties(records: Record<string, string | null>): Promise<void>--><!--Device-MakerNoteHuaweiMetadata-setProperties(records: Record<string, string | null>): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| records | Record&lt;string, string \| null&gt; | 是 | 包含要修改的MakerNoteHuaweiMetadata对象属性键值对的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7600202](../errorcode-image.md#7600202-不支持的元数据读写) | Unsupported metadata. Possible causes: unsupported metadata type. |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function SetProperties(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // 图片包含exif metadata。
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
  let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
  if (metaData != null) {
    let setkey: Record<string, string | null> = {
      "ImageWidth": "200",
      "ImageLength": "300"
    };
    await metaData.setProperties(setkey).then(async () => {
      console.info('Succeeded in setting AuxPictureObj properties.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to set metadata Properties. code is ${error.code}, message is ${error.message}`);
    })
  } else {
    console.error('AuxPictureObj metadata is null. ');
  }
}
```

ArkTS-Sta示例:

```TypeScript
function SetPropertiesFunc(metadata: image.Metadata): void {
  let properties: Record<string, string | null> = {
    "ImageWidth": "200",
    "ImageLength": "300"
  };
  try {
    await metadata.setProperties(properties);
    console.info(0x00000, 'SetPropertiesFunc', 'setProperties success!');
  } catch (err) {
    console.error(0x00000, 'SetPropertiesFunc', 'SetPropertiesFunc failed: ' + err);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataSetProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    let setkey: Record<string, string | null> = {
      "ImageWidth": "200",
      "ImageLength": "300"
    };
    await metaData.exifMetadata.setProperties(setkey).then(async () => {
      console.info('Succeeded in setting properties.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to set metadata Properties. code is ${error.code}, message is ${error.message}`);
    })
  } else {
    console.error('metadata is null. ');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function exifMetadataSetProperties(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    try {
      const exif = metaData?.exifMetadata;
      let setkey: Record<string, string | null> = {
        "ImageWidth": "200",
        "ImageLength": "300"
      };
      if (exif) {
        let data = exif.setProperties(setkey);
        console.info('Set properties ',JSON.stringify(data));
      }
    } catch ( err ) {
      console.error(`Failed to set metadata Properties. code is ${err.code}, error.message is ${err.message}`);
    }
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function makerNoteHuaweiSetProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    let setkey: Record<string, string | null> = {
      "HwMnoteIsXmageSupported": "1",
      "HwMnoteXmageMode": "9"
    };
    await metaData.makerNoteHuaweiMetadata.setProperties(setkey).then(async () => {
      console.info('Succeeded in setting properties.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to set metadata Properties. code is ${error.code}, message is ${error.message}`);
    })
  } else {
    console.error('metadata is null. ');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // 图片包含exif metadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function makerNoteHuaweiMetadataSetProperties(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    try {
      const exif = metaData?.makerNoteHuaweiMetadata;
      let setkey: Record<string, string | null> = {
        "HwMnoteIsXmageSupported": "1",
        "HwMnoteXmageMode": "9"
      };
      if (exif) {
        let data = exif.setProperties(setkey);
        console.info('Set properties ',JSON.stringify(data));
      }
    } catch ( err ) {
      console.error(`Failed to set metadata Properties. code is ${err.code}, error.message is ${err.message}`);
    }
  } else {
    console.error('Metadata is null.');
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function heifsMetadataSetProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    let setkey: Record<string, string | null> = {
      "HeifsDelayTime": "200",
    };
    await metaData.heifsMetadata.setProperties(setkey).then(async () => {
      console.info('Succeeded in setting properties.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to set metadata Properties. code is ${error.code}, message is ${error.message}`);
    })
  } else {
    console.error('metadata is null. ');
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

function getFileFd(context: common.UIAbilityContext): int | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // 图片包含HeifsMetadata。
  const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
  const fd = file.fd;
  return fd;
}

async function heifsMetadataSetProperties(context: common.UIAbilityContext) {
  let fd = getFileFd(context);
  if (fd == undefined) {
    return;
  }
  let imageSource = image.createImageSource(fd);
  if (imageSource == null) {
    return;
  }
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    try {
      const exif = metaData?.heifsMetadata;
      let setkey: Record<string, string | null> = {
        "HeifsDelayTime": "200",
      };
      if (exif) {
        let data = exif.setProperties(setkey);
        console.info('Set properties ',JSON.stringify(data));
      }
    } catch ( err ) {
      console.error(`Failed to set metadata Properties. code is ${err.code}, error.message is ${err.message}`);
    }
  } else {
    console.error('Metadata is null.');
  }
}
```

## burstNumber

```TypeScript
burstNumber?: int
```

连拍数量。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-burstNumber?: int--><!--Device-MakerNoteHuaweiMetadata-burstNumber?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## captureMode

```TypeScript
captureMode?: int
```

捕获模式。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-captureMode?: int--><!--Device-MakerNoteHuaweiMetadata-captureMode?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## cloudLabel

```TypeScript
cloudLabel?: string
```

云增强标签。

**类型：** string

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-cloudLabel?: string--><!--Device-MakerNoteHuaweiMetadata-cloudLabel?: string-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## faceConfidences

```TypeScript
faceConfidences?: int[]
```

对指定数量的面孔置信度。

**类型：** int[]

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-faceConfidences?: int[]--><!--Device-MakerNoteHuaweiMetadata-faceConfidences?: int[]-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## faceCount

```TypeScript
faceCount?: int
```

人脸数。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-faceCount?: int--><!--Device-MakerNoteHuaweiMetadata-faceCount?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## faceSmileScores

```TypeScript
faceSmileScores?: int[]
```

特定数量面孔的微笑得分。

**类型：** int[]

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-faceSmileScores?: int[]--><!--Device-MakerNoteHuaweiMetadata-faceSmileScores?: int[]-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## focusMode

```TypeScript
focusMode?: FocusMode
```

镜头对焦控制策略，决定相机如何调整焦距。

**类型：** FocusMode

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-focusMode?: FocusMode--><!--Device-MakerNoteHuaweiMetadata-focusMode?: FocusMode-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## isCloudEnhanced

```TypeScript
isCloudEnhanced?: boolean
```

图像是否存在云端增强。true表示存在，false表示不存在。

**类型：** boolean

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-isCloudEnhanced?: boolean--><!--Device-MakerNoteHuaweiMetadata-isCloudEnhanced?: boolean-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## isFrontCamera

```TypeScript
isFrontCamera?: boolean
```

是否使用前置摄像头。true表示使用，false表示不使用。

**类型：** boolean

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-isFrontCamera?: boolean--><!--Device-MakerNoteHuaweiMetadata-isFrontCamera?: boolean-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## isWindSnapshot

```TypeScript
isWindSnapshot?: boolean
```

是否采用风快照模式拍摄。true表示采用，false表示不采用。该模式是针对拍摄快速移动物体或容易产生模糊场景（如大风中、抓拍运动物体）的专门摄影。

**类型：** boolean

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-isWindSnapshot?: boolean--><!--Device-MakerNoteHuaweiMetadata-isWindSnapshot?: boolean-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## isXmageSupported

```TypeScript
isXmageSupported?: boolean
```

是否支持XMAGE。true表示支持，false表示不支持。

**类型：** boolean

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-isXmageSupported?: boolean--><!--Device-MakerNoteHuaweiMetadata-isXmageSupported?: boolean-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## physicalAperture

```TypeScript
physicalAperture?: int
```

物理光圈值。单位是fNumber。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-physicalAperture?: int--><!--Device-MakerNoteHuaweiMetadata-physicalAperture?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## pitchAngle

```TypeScript
pitchAngle?: int
```

俯仰角度。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-pitchAngle?: int--><!--Device-MakerNoteHuaweiMetadata-pitchAngle?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## rollAngle

```TypeScript
rollAngle?: int
```

左右滚动角度。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-rollAngle?: int--><!--Device-MakerNoteHuaweiMetadata-rollAngle?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## sceneBeachConfidence

```TypeScript
sceneBeachConfidence?: int
```

拍摄场景：海滩置信度。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-sceneBeachConfidence?: int--><!--Device-MakerNoteHuaweiMetadata-sceneBeachConfidence?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## sceneBlueSkyConfidence

```TypeScript
sceneBlueSkyConfidence?: int
```

拍摄场景：蓝天置信度。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-sceneBlueSkyConfidence?: int--><!--Device-MakerNoteHuaweiMetadata-sceneBlueSkyConfidence?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## sceneFlowersConfidence

```TypeScript
sceneFlowersConfidence?: int
```

拍摄场景：花卉置信度。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-sceneFlowersConfidence?: int--><!--Device-MakerNoteHuaweiMetadata-sceneFlowersConfidence?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## sceneFoodConfidence

```TypeScript
sceneFoodConfidence?: int
```

拍摄场景：美食置信度。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-sceneFoodConfidence?: int--><!--Device-MakerNoteHuaweiMetadata-sceneFoodConfidence?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## sceneGreenPlantConfidence

```TypeScript
sceneGreenPlantConfidence?: int
```

拍摄场景：绿色植物置信度。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-sceneGreenPlantConfidence?: int--><!--Device-MakerNoteHuaweiMetadata-sceneGreenPlantConfidence?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## sceneNightConfidence

```TypeScript
sceneNightConfidence?: int
```

拍摄场景：夜景置信度。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-sceneNightConfidence?: int--><!--Device-MakerNoteHuaweiMetadata-sceneNightConfidence?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## sceneSnowConfidence

```TypeScript
sceneSnowConfidence?: int
```

拍摄场景：雪景置信度。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-sceneSnowConfidence?: int--><!--Device-MakerNoteHuaweiMetadata-sceneSnowConfidence?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## sceneStageConfidence

```TypeScript
sceneStageConfidence?: int
```

拍摄场景：舞台演出置信度。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-sceneStageConfidence?: int--><!--Device-MakerNoteHuaweiMetadata-sceneStageConfidence?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## sceneSunsetConfidence

```TypeScript
sceneSunsetConfidence?: int
```

拍摄场景：日落置信度。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-sceneSunsetConfidence?: int--><!--Device-MakerNoteHuaweiMetadata-sceneSunsetConfidence?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## sceneTextConfidence

```TypeScript
sceneTextConfidence?: int
```

拍摄场景：文本置信度。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-sceneTextConfidence?: int--><!--Device-MakerNoteHuaweiMetadata-sceneTextConfidence?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## sceneVersion

```TypeScript
sceneVersion?: int
```

场景识别算法版本号。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-sceneVersion?: int--><!--Device-MakerNoteHuaweiMetadata-sceneVersion?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## xmageBottom

```TypeScript
xmageBottom?: int
```

当照片包含XMAGE水印时，原始图片上，有效内容区域（不含水印覆盖范围）的下边界（相对于图片左上角原点）的垂直坐标。单位为像素（px）。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-xmageBottom?: int--><!--Device-MakerNoteHuaweiMetadata-xmageBottom?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## xmageColorMode

```TypeScript
xmageColorMode?: XmageColorMode
```

XMAGE颜色模式。

**类型：** [XmageColorMode](arkts-image-image-xmagecolormode-e.md)

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-xmageColorMode?: XmageColorMode--><!--Device-MakerNoteHuaweiMetadata-xmageColorMode?: XmageColorMode-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## xmageLeft

```TypeScript
xmageLeft?: int
```

当照片包含XMAGE水印时，原始图片上，有效内容区域（不含水印覆盖范围）的左边界（相对于图片左上角原点）的水平坐标。单位为像素（px）。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-xmageLeft?: int--><!--Device-MakerNoteHuaweiMetadata-xmageLeft?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## xmageRight

```TypeScript
xmageRight?: int
```

当照片包含XMAGE水印时，原始图片上，有效内容区域（不含水印覆盖范围）的右边界（相对于图片左上角原点）的水平坐标。单位为像素（px）。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-xmageRight?: int--><!--Device-MakerNoteHuaweiMetadata-xmageRight?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## xmageTop

```TypeScript
xmageTop?: int
```

当照片包含XMAGE水印时，原始图片上，有效内容区域（不含水印覆盖范围）的上边界（相对于图片左上角原点）的垂直坐标。单位为像素（px）。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-xmageTop?: int--><!--Device-MakerNoteHuaweiMetadata-xmageTop?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## xmageWatermarkMode

```TypeScript
xmageWatermarkMode?: int
```

XMAGE水印模式。具体取值请参考[Constants](arkts-multimedia-image.md)。

**类型：** int

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MakerNoteHuaweiMetadata-xmageWatermarkMode?: int--><!--Device-MakerNoteHuaweiMetadata-xmageWatermarkMode?: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

