# ExifMetadata

ExifMetadata implements Metadata Exchangeable Image File Format (Exif) metadata.

**Inheritance/Implementation:** ExifMetadata implements [Metadata](arkts-image-image-metadata-i.md)

**Since:** 23

<!--Device-image-class ExifMetadata--><!--Device-image-class ExifMetadata-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## clone

```TypeScript
clone(): Promise<ExifMetadata>
```

Clones the Exif metadata. This API returns the result asynchronously through a promise.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-clone(): Promise<ExifMetadata>--><!--Device-ExifMetadata-clone(): Promise<ExifMetadata>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ExifMetadata](arkts-image-image-exifmetadata-c.md)&gt; | Promise used to return the Exif metadata instance if the operation is successful. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Clone(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
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
      console.error(`Clone new_metadata failed, error : ${err}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info(`Clone new_metadata and get Properties: ${data1}`);
    }).catch((err: BusinessError) => {
      console.error(`Clone new_metadata failed, error : ${err}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info(`Clone new_metadata and get Properties: ${data1}`);
    }).catch((err: BusinessError) => {
      console.error(`Clone new_metadata failed, error : ${err}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // An image containing HeifsMetadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info(`Clone new_metadata and get Properties: ${data1}`);
    }).catch((err: BusinessError) => {
      console.error(`Clone new_metadata failed, error : ${err}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Clone(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.clone().then((clonePixelMap: image.PixelMap) => {
      console.info('Succeeded clone pixelmap.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to clone pixelmap. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

## createInstance

```TypeScript
static createInstance(): ExifMetadata
```

Creates an empty [ExifMetadata](#exifmetadata) instance.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-static createInstance(): ExifMetadata--><!--Device-ExifMetadata-static createInstance(): ExifMetadata-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ExifMetadata](arkts-image-image-exifmetadata-c.md) | Empty **ExifMetadata** instance. |

**Examples**

```TypeScript
async function exifMetadataCreateInstance(context: Context) {
  let exifMetadata = image.ExifMetadata.createInstance();
  if (exifMetadata != undefined) {
    console.info("createInstance success");
  }
}
```

```TypeScript
async function makerNoteHuaweiCreateInstance(context: Context) {
  let makerNoteHuaweiMetadata = image.MakerNoteHuaweiMetadata.createInstance();
  if (makerNoteHuaweiMetadata != undefined) {
    console.info("createInstance success");
  }
}
```

```TypeScript
async function heifsMetadataCreateInstance(context: Context) {
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

Obtains all properties and their values from the image metadata. This API returns the result asynchronously through a promise.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-getAllProperties(): Promise<Record<string, string | null>>--><!--Device-ExifMetadata-getAllProperties(): Promise<Record<string, string | null>>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Record&lt;string, string \| null&gt;&gt; | Promise used to return the values of all properties. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetAllProperties(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
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
      console.error(`Get metadata all properties failed error.code is ${error.code}, error.message is ${error.message}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info('Metadata have ', count, ' properties');
      console.info(`Get metadata all properties: ${data}`);
    }).catch((error: BusinessError) => {
      console.error(`Get metadata all properties failed error.code is ${error.code}, error.message is ${error.message}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info(`Get metadata all properties: ${data}`);
    }).catch((error: BusinessError) => {
      console.error(`Get metadata all properties failed error.code is ${error.code}, error.message is ${error.message}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // An image containing HeifsMetadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info('Metadata have ', count, ' properties');
      console.info(`Get metadata all properties: ${data}`);
    }).catch((error: BusinessError) => {
      console.error(`Get metadata all properties failed error.code is ${error.code}, error.message is ${error.message}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

## getBlob

```TypeScript
getBlob(): Promise<ArrayBuffer>
```

Obtains the metadata in binary format. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-getBlob(): Promise<ArrayBuffer>--><!--Device-ExifMetadata-getBlob(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise that returns the binary data of the metadata. |

**Examples**

```TypeScript
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg'; // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info("get blob success");
    }
  }
}
```

```TypeScript
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info("get blob success");
    }
  }
}
```

```TypeScript
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info("get blob success");
    }
  }
}
```

```TypeScript
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // An image containing HeifsMetadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info("get blob success");
    }
  }
}
```

## getProperties

```TypeScript
getProperties(key: Array<string>): Promise<Record<string, string | null>>
```

Obtains the property values from image metadata. This API returns the result asynchronously through a promise.For details about the properties, see [PropertyKey](arkts-image-image-propertykey-e.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-getProperties(key: Array<string>): Promise<Record<string, string | null>>--><!--Device-ExifMetadata-getProperties(key: Array<string>): Promise<Record<string, string | null>>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | Array&lt;string&gt; | Yes | Names of the properties to query. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Record&lt;string, string \| null&gt;&gt; | Promise used to return the obtained image metadata property values. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) | Unsupported metadata. Possible causes: unsupported metadata type. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetProperties(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
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
      console.error(`Get properties failed error.code is ${error.code}, error.message is ${error.message}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function exifMetadataGetProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["ImageWidth", "ImageLength"]);
  if (metaData != undefined && metaData.exifMetadata != undefined) {
    await metaData.exifMetadata.getProperties(["ImageWidth", "ImageLength"]).then((data) => {
      console.info('Get properties ',JSON.stringify(data));
    }).catch((error: BusinessError) => {
      console.error(`Get properties failed error.code is ${error.code}, error.message is ${error.message}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function makerNoteHuaweiGetProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]);
  if (metaData != undefined && metaData.makerNoteHuaweiMetadata != undefined) {
    await metaData.makerNoteHuaweiMetadata.getProperties(["HwMnoteIsXmageSupported", "HwMnoteXmageMode"]).then((data) => {
      console.info('Get properties ',JSON.stringify(data));
    }).catch((error: BusinessError) => {
      console.error(`Get properties failed error.code is ${error.code}, error.message is ${error.message}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // An image containing HeifsMetadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
  const fd: number = file?.fd;
  return fd;
}

async function heifsMetadataGetProperties(context: Context) {
  let fd = getFileFd(context);
  let imageSource = image.createImageSource(fd);
  let metaData = await imageSource.readImageMetadata(["HeifsDelayTime"]);
  if (metaData != undefined && metaData.heifsMetadata != undefined) {
    await metaData.heifsMetadata.getProperties(["HeifsDelayTime"]).then((data) => {
      console.info('Get properties ',JSON.stringify(data));
    }).catch((error: BusinessError) => {
      console.error(`Get properties failed error.code is ${error.code}, error.message is ${error.message}`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
```

## setBlob

```TypeScript
setBlob(blob: ArrayBuffer): Promise<void>
```

Replaces the current metadata with binary data. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-setBlob(blob: ArrayBuffer): Promise<void>--><!--Device-ExifMetadata-setBlob(blob: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blob | ArrayBuffer | Yes | Binary data used to replace the metadata. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible causes: The blob is empty or has a length of 0. |

**Examples**

```TypeScript
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info("get blob success");
      metaData.setBlob(blob);
    }
    let new_blob = metaData.getBlob();
    if (new_blob != undefined) {
      console.info("new_blob is not undefined");
    }
  }
}
```

```TypeScript
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info("get blob success");
      metaData.exifMetadata.setBlob(blob);
    }
    let new_blob = metaData.exifMetadata.getBlob();
    if (new_blob != undefined) {
      console.info("new_blob is not undefined");
    }
  }
}
```

```TypeScript
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info("get blob success");
      metaData.makerNoteHuaweiMetadata.setBlob(blob);
    }
    let new_blob = metaData.makerNoteHuaweiMetadata.getBlob();
    if (new_blob != undefined) {
      console.info("new_blob is not undefined");
    }
  }
}
```

```TypeScript
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // An image containing HeifsMetadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info("get blob success");
      metaData.heifsMetadata.setBlob(blob);
    }
    let new_blob = metaData.heifsMetadata.getBlob();
    if (new_blob != undefined) {
      console.info("new_blob is not undefined");
    }
  }
}
```

## setProperties

```TypeScript
setProperties(records: Record<string, string | null>): Promise<void>
```

Sets the values of specified properties in image metadata in batches. This API returns the result asynchronously through a promise.For details about the properties, see [PropertyKey](arkts-image-image-propertykey-e.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-setProperties(records: Record<string, string | null>): Promise<void>--><!--Device-ExifMetadata-setProperties(records: Record<string, string | null>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| records | Record&lt;string, string \| null&gt; | Yes | Set of key-value pairs representing properties and corresponding values of the **ExifMetadata** object. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) | Unsupported metadata. Possible causes: unsupported metadata type. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function SetProperties(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
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
      console.info('Set AuxPictureObj properties success.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to set metadata Properties. code is ${error.code}, message is ${error.message}`);
    })
  } else {
    console.error('AuxPictureObj metadata is null. ');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info('Set properties success.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to set metadata Properties. code is ${error.code}, message is ${error.message}`);
    })
  } else {
    console.error('metadata is null. ');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/exif.jpg';  // An image containing Exif metadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info('Set properties success.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to set metadata Properties. code is ${error.code}, message is ${error.message}`);
    })
  } else {
    console.error('metadata is null. ');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

function getFileFd(context: Context): number | undefined {
  const filePath: string = context.cacheDir + '/heifs.heic';  // An image containing HeifsMetadata is required.
  const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_WRITE);
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
      console.info('Set properties success.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to set metadata Properties. code is ${error.code}, message is ${error.message}`);
    })
  } else {
    console.error('metadata is null. ');
  }
}
```

## apertureValue

```TypeScript
apertureValue?: double
```

Lens aperture. The unit is APEX.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-apertureValue?: double--><!--Device-ExifMetadata-apertureValue?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## artist

```TypeScript
artist?: string
```

Name of the person who creates the image.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-artist?: string--><!--Device-ExifMetadata-artist?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## bitsPerSample

```TypeScript
bitsPerSample?: int[]
```

Number of bits for each pixel component. For example, RGB has 3 components with a format of 8,8,8.

**Type:** int[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-bitsPerSample?: int[]--><!--Device-ExifMetadata-bitsPerSample?: int[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## bodySerialNumber

```TypeScript
bodySerialNumber?: string
```

Serial number of the camera body.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-bodySerialNumber?: string--><!--Device-ExifMetadata-bodySerialNumber?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## brightnessValue

```TypeScript
brightnessValue?: double
```

Image brightness. The unit is APEX.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-brightnessValue?: double--><!--Device-ExifMetadata-brightnessValue?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## cameraOwnerName

```TypeScript
cameraOwnerName?: string
```

Name of the camera owner.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-cameraOwnerName?: string--><!--Device-ExifMetadata-cameraOwnerName?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## cfaPattern

```TypeScript
cfaPattern?: ArrayBuffer
```

Color filter array (CFA) geometric pattern of the image sensor.

**Type:** ArrayBuffer

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-cfaPattern?: ArrayBuffer--><!--Device-ExifMetadata-cfaPattern?: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## colorSpace

```TypeScript
colorSpace?: int
```

Color space information, which is usually recorded as a color space descriptor. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-colorSpace?: int--><!--Device-ExifMetadata-colorSpace?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## componentsConfiguration

```TypeScript
componentsConfiguration?: string
```

Information about the compressed data.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-componentsConfiguration?: string--><!--Device-ExifMetadata-componentsConfiguration?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## compositeImage

```TypeScript
compositeImage?: int
```

Whether the image is a composite image. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-compositeImage?: int--><!--Device-ExifMetadata-compositeImage?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## compressedBitsPerPixel

```TypeScript
compressedBitsPerPixel?: double
```

Image compression scheme. The unit is bit/pixel.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-compressedBitsPerPixel?: double--><!--Device-ExifMetadata-compressedBitsPerPixel?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## compression

```TypeScript
compression?: int
```

Algorithm standard for image compression. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-compression?: int--><!--Device-ExifMetadata-compression?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## contrast

```TypeScript
contrast?: int
```

Contrast optimization policy applied by the camera. For example, standard processing and contrast reduction. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-contrast?: int--><!--Device-ExifMetadata-contrast?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## copyright

```TypeScript
copyright?: string
```

Copyright notice of the image.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-copyright?: string--><!--Device-ExifMetadata-copyright?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## customRendered

```TypeScript
customRendered?: int
```

Special processing of image data, such as HDR composition and AI scene enhancement. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-customRendered?: int--><!--Device-ExifMetadata-customRendered?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## dateTime

```TypeScript
dateTime?: string
```

Date and time when the image is created. In this standard, it refers to the file date and time. The value format is *YYYY:MM:DD HH:MM:SS* (24-hour clock). For example, 2025:12:15 18:44:59.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-dateTime?: string--><!--Device-ExifMetadata-dateTime?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## dateTimeDigitized

```TypeScript
dateTimeDigitized?: string
```

Date and time when the image is stored as digital data. For example, if a DSC captures an image and records the file at the same time, the values of **DateTimeOriginal** and **DateTimeDigitized** are the same. The value format is *YYYY:MM:DD HH:MM:SS* (24-hour clock).

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-dateTimeDigitized?: string--><!--Device-ExifMetadata-dateTimeDigitized?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## dateTimeOriginal

```TypeScript
dateTimeOriginal?: string
```

Date and time when the original image data is generated. For a digital still camera (DSC), the date and time when a photo is taken are recorded. The value format is *YYYY:MM:DD HH:MM:SS* (24-hour clock).

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-dateTimeOriginal?: string--><!--Device-ExifMetadata-dateTimeOriginal?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## deviceSettingDescription

```TypeScript
deviceSettingDescription?: ArrayBuffer
```

Capture condition information of a specific camera model.

**Type:** ArrayBuffer

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-deviceSettingDescription?: ArrayBuffer--><!--Device-ExifMetadata-deviceSettingDescription?: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## digitalZoomRatio

```TypeScript
digitalZoomRatio?: double
```

Digital zoom ratio used when the image is captured.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-digitalZoomRatio?: double--><!--Device-ExifMetadata-digitalZoomRatio?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## exifVersion

```TypeScript
exifVersion?: string
```

Version of the supported Exif standard.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-exifVersion?: string--><!--Device-ExifMetadata-exifVersion?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## exposureBiasValue

```TypeScript
exposureBiasValue?: double
```

Exposure bias.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-exposureBiasValue?: double--><!--Device-ExifMetadata-exposureBiasValue?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## exposureIndex

```TypeScript
exposureIndex?: double
```

Exposure index selected at the time the image is captured.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-exposureIndex?: double--><!--Device-ExifMetadata-exposureIndex?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## exposureMode

```TypeScript
exposureMode?: int
```

Exposure mode. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-exposureMode?: int--><!--Device-ExifMetadata-exposureMode?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## exposureProgram

```TypeScript
exposureProgram?: int
```

Class used for exposure setting when the camera captures a photo. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-exposureProgram?: int--><!--Device-ExifMetadata-exposureProgram?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## exposureTime

```TypeScript
exposureTime?: double
```

Exposure time.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-exposureTime?: double--><!--Device-ExifMetadata-exposureTime?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## fileSource

```TypeScript
fileSource?: ArrayBuffer
```

Image source.

**Type:** ArrayBuffer

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-fileSource?: ArrayBuffer--><!--Device-ExifMetadata-fileSource?: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## flash

```TypeScript
flash?: int
```

Flash. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-flash?: int--><!--Device-ExifMetadata-flash?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## flashEnergy

```TypeScript
flashEnergy?: double
```

Flash energy at the time the image is captured. The unit is beam candlepower seconds (BCPS).

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-flashEnergy?: double--><!--Device-ExifMetadata-flashEnergy?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## flashpixVersion

```TypeScript
flashpixVersion?: string
```

FlashPix format version supported by the FlashPix Extension Resource (FPXR), which is used to enhance device compatibility.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-flashpixVersion?: string--><!--Device-ExifMetadata-flashpixVersion?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## fNumber

```TypeScript
fNumber?: double
```

F number, for example, f/1.8.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-fNumber?: double--><!--Device-ExifMetadata-fNumber?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## focalLength

```TypeScript
focalLength?: double
```

Focal length of the lens, in milliseconds.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-focalLength?: double--><!--Device-ExifMetadata-focalLength?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## focalLengthIn35mmFilm

```TypeScript
focalLengthIn35mmFilm?: int
```

Focal length of the 35 mm film. The value should be an integer.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-focalLengthIn35mmFilm?: int--><!--Device-ExifMetadata-focalLengthIn35mmFilm?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## focalPlaneResolutionUnit

```TypeScript
focalPlaneResolutionUnit?: int
```

Measurement unit of **FocalPlaneXResolution** and **FocalPlaneYResolution**. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-focalPlaneResolutionUnit?: int--><!--Device-ExifMetadata-focalPlaneResolutionUnit?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## focalPlaneXResolution

```TypeScript
focalPlaneXResolution?: double
```

Number of pixels per unit physical length in the X-axis of the sensor's physical plane.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-focalPlaneXResolution?: double--><!--Device-ExifMetadata-focalPlaneXResolution?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## focalPlaneYResolution

```TypeScript
focalPlaneYResolution?: double
```

Number of pixels per unit physical length in the Y-axis of the sensor's physical plane.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-focalPlaneYResolution?: double--><!--Device-ExifMetadata-focalPlaneYResolution?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gainControl

```TypeScript
gainControl?: int
```

Degree of overall image gain adjustment. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gainControl?: int--><!--Device-ExifMetadata-gainControl?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gamma

```TypeScript
gamma?: double
```

Gamma value of each component.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gamma?: double--><!--Device-ExifMetadata-gamma?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsAltitude

```TypeScript
gpsAltitude?: double
```

GPS altitude based on **GPSAltitudeRef**.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsAltitude?: double--><!--Device-ExifMetadata-gpsAltitude?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsAltitudeRef

```TypeScript
gpsAltitudeRef?: int
```

GPS altitude reference. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsAltitudeRef?: int--><!--Device-ExifMetadata-gpsAltitudeRef?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsAreaInformation

```TypeScript
gpsAreaInformation?: string
```

String of the GPS area name.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsAreaInformation?: string--><!--Device-ExifMetadata-gpsAreaInformation?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsDateStamp

```TypeScript
gpsDateStamp?: string
```

GPS date stamp.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsDateStamp?: string--><!--Device-ExifMetadata-gpsDateStamp?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsDestBearing

```TypeScript
gpsDestBearing?: double
```

Bearing to the destination.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsDestBearing?: double--><!--Device-ExifMetadata-gpsDestBearing?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsDestBearingRef

```TypeScript
gpsDestBearingRef?: string
```

Bearing reference to the destination.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsDestBearingRef?: string--><!--Device-ExifMetadata-gpsDestBearingRef?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsDestDistance

```TypeScript
gpsDestDistance?: double
```

Distance to the destination.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsDestDistance?: double--><!--Device-ExifMetadata-gpsDestDistance?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsDestDistanceRef

```TypeScript
gpsDestDistanceRef?: string
```

Unit used to express the distance to the destination.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsDestDistanceRef?: string--><!--Device-ExifMetadata-gpsDestDistanceRef?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsDestLatitude

```TypeScript
gpsDestLatitude?: double[]
```

Latitude of the destination.

**Type:** double[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsDestLatitude?: double[]--><!--Device-ExifMetadata-gpsDestLatitude?: double[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsDestLatitudeRef

```TypeScript
gpsDestLatitudeRef?: string
```

Latitude reference of the destination.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsDestLatitudeRef?: string--><!--Device-ExifMetadata-gpsDestLatitudeRef?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsDestLongitude

```TypeScript
gpsDestLongitude?: double[]
```

Longitude of the destination.

**Type:** double[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsDestLongitude?: double[]--><!--Device-ExifMetadata-gpsDestLongitude?: double[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsDestLongitudeRef

```TypeScript
gpsDestLongitudeRef?: string
```

Longitude reference of the destination.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsDestLongitudeRef?: string--><!--Device-ExifMetadata-gpsDestLongitudeRef?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsDifferential

```TypeScript
gpsDifferential?: int
```

Whether differential correction has been applied to the GPS data, which is crucial for precise positioning accuracy. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsDifferential?: int--><!--Device-ExifMetadata-gpsDifferential?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsDop

```TypeScript
gpsDop?: double
```

Dilution of Precision (DOP) of the GPS data.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsDop?: double--><!--Device-ExifMetadata-gpsDop?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsHPositioningError

```TypeScript
gpsHPositioningError?: double
```

Horizontal positioning error, in meters.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsHPositioningError?: double--><!--Device-ExifMetadata-gpsHPositioningError?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsImgDirection

```TypeScript
gpsImgDirection?: double
```

Image orientation at the time of capture.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsImgDirection?: double--><!--Device-ExifMetadata-gpsImgDirection?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsImgDirectionRef

```TypeScript
gpsImgDirectionRef?: string
```

Reference of the image orientation.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsImgDirectionRef?: string--><!--Device-ExifMetadata-gpsImgDirectionRef?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsLatitude

```TypeScript
gpsLatitude?: double[]
```

GPS latitude. The latitude is represented by three RATIONAL values (numeric values stored in fractional form), corresponding to degrees, minutes, and seconds, in the **dd/1, mm/1, ss/1** format. When using degrees and minutes, the minutes are stored with up to two decimal places, in the **dd/1, mmmm/100, 0/1** format.

**Type:** double[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsLatitude?: double[]--><!--Device-ExifMetadata-gpsLatitude?: double[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsLatitudeRef

```TypeScript
gpsLatitudeRef?: string
```

GPS latitude reference. For example, **N** indicates north latitude, and **S** indicates south latitude.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsLatitudeRef?: string--><!--Device-ExifMetadata-gpsLatitudeRef?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsLongitude

```TypeScript
gpsLongitude?: double[]
```

GPS longitude. The longitude is represented by three RATIONAL values (numeric values stored in fractional form), corresponding to degrees, minutes, and seconds, in the **dd/1, mm/1, ss/1** format. When using degrees and minutes, the minutes are stored with up to two decimal places, in the **dd/1, mmmm/100, 0/1** format.

**Type:** double[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsLongitude?: double[]--><!--Device-ExifMetadata-gpsLongitude?: double[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsLongitudeRef

```TypeScript
gpsLongitudeRef?: string
```

GPS longitude reference. For example, **E** indicates east longitude, and **W** indicates west longitude.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsLongitudeRef?: string--><!--Device-ExifMetadata-gpsLongitudeRef?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsMapDatum

```TypeScript
gpsMapDatum?: string
```

Geodetic data used by the GPS receiver.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsMapDatum?: string--><!--Device-ExifMetadata-gpsMapDatum?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsMeasureMode

```TypeScript
gpsMeasureMode?: string
```

GPS measurement mode.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsMeasureMode?: string--><!--Device-ExifMetadata-gpsMeasureMode?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsProcessingMethod

```TypeScript
gpsProcessingMethod?: string
```

Name of the positioning method.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsProcessingMethod?: string--><!--Device-ExifMetadata-gpsProcessingMethod?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsSatellites

```TypeScript
gpsSatellites?: string
```

GPS satellite used for measurement. Generally, the value is the GPS satellite's pseudo-random noise (PRN) number.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsSatellites?: string--><!--Device-ExifMetadata-gpsSatellites?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsSpeed

```TypeScript
gpsSpeed?: double
```

Speed of the GPS receiver.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsSpeed?: double--><!--Device-ExifMetadata-gpsSpeed?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsSpeedRef

```TypeScript
gpsSpeedRef?: string
```

Speed unit of the GPS receiver.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsSpeedRef?: string--><!--Device-ExifMetadata-gpsSpeedRef?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsStatus

```TypeScript
gpsStatus?: string
```

Status of the GPS receiver when the image is recorded.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsStatus?: string--><!--Device-ExifMetadata-gpsStatus?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsTimestamp

```TypeScript
gpsTimestamp?: double[]
```

GPS timestamp.

**Type:** double[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsTimestamp?: double[]--><!--Device-ExifMetadata-gpsTimestamp?: double[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsTrack

```TypeScript
gpsTrack?: double
```

Movement direction of the GPS receiver.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsTrack?: double--><!--Device-ExifMetadata-gpsTrack?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsTrackRef

```TypeScript
gpsTrackRef?: string
```

Reference for the GPS receiver movement direction.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsTrackRef?: string--><!--Device-ExifMetadata-gpsTrackRef?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## gpsVersionID

```TypeScript
gpsVersionID?: int[]
```

GPS information format version identifier.

**Type:** int[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-gpsVersionID?: int[]--><!--Device-ExifMetadata-gpsVersionID?: int[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## imageDescription

```TypeScript
imageDescription?: string
```

Image description.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-imageDescription?: string--><!--Device-ExifMetadata-imageDescription?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## imageLength

```TypeScript
imageLength?: int
```

Image length. The unit is px.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-imageLength?: int--><!--Device-ExifMetadata-imageLength?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## imageUniqueId

```TypeScript
imageUniqueId?: string
```

Unique ID assigned to each image.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-imageUniqueId?: string--><!--Device-ExifMetadata-imageUniqueId?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## imageWidth

```TypeScript
imageWidth?: int
```

Image width. The unit is px.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-imageWidth?: int--><!--Device-ExifMetadata-imageWidth?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## isoSpeedLatitudeyyy

```TypeScript
isoSpeedLatitudeyyy?: int
```

Maximum dynamic range recordable by the camera sensor in a single exposure. The unit is EV. The value should be an integer.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-isoSpeedLatitudeyyy?: int--><!--Device-ExifMetadata-isoSpeedLatitudeyyy?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## isoSpeedLatitudezzz

```TypeScript
isoSpeedLatitudezzz?: int
```

Highlight retention capacity of the camera sensor in overexposure. The unit is EV. The value should be an integer.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-isoSpeedLatitudezzz?: int--><!--Device-ExifMetadata-isoSpeedLatitudezzz?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## isoSpeedRatings

```TypeScript
isoSpeedRatings?: int
```

ISO speed and latitude of the camera or input device, which are specified in ISO 12232. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-isoSpeedRatings?: int--><!--Device-ExifMetadata-isoSpeedRatings?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## jpegInterchangeFormat

```TypeScript
jpegInterchangeFormat?: int
```

Start of Image (SOI) marker of the JPEG bitstream in interchange format. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-jpegInterchangeFormat?: int--><!--Device-ExifMetadata-jpegInterchangeFormat?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## jpegInterchangeFormatLength

```TypeScript
jpegInterchangeFormatLength?: int
```

Number of bytes in the JPEG stream. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-jpegInterchangeFormatLength?: int--><!--Device-ExifMetadata-jpegInterchangeFormatLength?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## lensMake

```TypeScript
lensMake?: string
```

Manufacturer of the lens.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-lensMake?: string--><!--Device-ExifMetadata-lensMake?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## lensModel

```TypeScript
lensModel?: string
```

Model of the lens.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-lensModel?: string--><!--Device-ExifMetadata-lensModel?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## lensSerialNumber

```TypeScript
lensSerialNumber?: string
```

Serial number of the lens.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-lensSerialNumber?: string--><!--Device-ExifMetadata-lensSerialNumber?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## lensSpecification

```TypeScript
lensSpecification?: double[]
```

Specifications of the lens.

**Type:** double[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-lensSpecification?: double[]--><!--Device-ExifMetadata-lensSpecification?: double[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## lightSource

```TypeScript
lightSource?: int
```

Light source. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-lightSource?: int--><!--Device-ExifMetadata-lightSource?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## make

```TypeScript
make?: string
```

Manufacturer name of the capture device.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-make?: string--><!--Device-ExifMetadata-make?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## makerNote

```TypeScript
makerNote?: ArrayBuffer
```

Information required by the Exif/Design rule for Camera File system (DCF) writer manufacturer.

**Type:** ArrayBuffer

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-makerNote?: ArrayBuffer--><!--Device-ExifMetadata-makerNote?: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## maxApertureValue

```TypeScript
maxApertureValue?: double
```

Minimum aperture value of the lens.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-maxApertureValue?: double--><!--Device-ExifMetadata-maxApertureValue?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## meteringMode

```TypeScript
meteringMode?: int
```

Metering mode. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-meteringMode?: int--><!--Device-ExifMetadata-meteringMode?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## model

```TypeScript
model?: string
```

Camera model.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-model?: string--><!--Device-ExifMetadata-model?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## newSubfileType

```TypeScript
newSubfileType?: int
```

Data type of a subfile (for example, basic types such as text or image, rather than specific storage formats). The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-newSubfileType?: int--><!--Device-ExifMetadata-newSubfileType?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## oecf

```TypeScript
oecf?: ArrayBuffer
```

Opto-Electric Conversion Function (OECF) specified in ISO 14524.

**Type:** ArrayBuffer

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-oecf?: ArrayBuffer--><!--Device-ExifMetadata-oecf?: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## offsetTime

```TypeScript
offsetTime?: string
```

Geographical time zone of the device.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-offsetTime?: string--><!--Device-ExifMetadata-offsetTime?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## offsetTimeDigitized

```TypeScript
offsetTimeDigitized?: string
```

Coordinated Universal Time (UTC) offset at the time of image digitization, which helps to precisely adjust the timestamp.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-offsetTimeDigitized?: string--><!--Device-ExifMetadata-offsetTimeDigitized?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## offsetTimeOriginal

```TypeScript
offsetTimeOriginal?: string
```

Geographical time zone of the device.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-offsetTimeOriginal?: string--><!--Device-ExifMetadata-offsetTimeOriginal?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## orientation

```TypeScript
orientation?: Orientation
```

Image orientation.

**Type:** Orientation

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-orientation?: Orientation--><!--Device-ExifMetadata-orientation?: Orientation-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## photographicSensitivity

```TypeScript
photographicSensitivity?: int[]
```

Sensitivity of the camera or input device during image capture.

**Type:** int[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-photographicSensitivity?: int[]--><!--Device-ExifMetadata-photographicSensitivity?: int[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## photometricInterpretation

```TypeScript
photometricInterpretation?: int
```

Pixel composition, such as RGB (Red, Green, Blue) and YCbCr (Luma, Blue-difference Chroma, Red-difference Chroma). The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-photometricInterpretation?: int--><!--Device-ExifMetadata-photometricInterpretation?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## photoMode

```TypeScript
photoMode?: int
```

Image mode. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-photoMode?: int--><!--Device-ExifMetadata-photoMode?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## pixelXDimension

```TypeScript
pixelXDimension?: int
```

Image size on the X axis (horizontal axis in a two-dimensional coordinate system). The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-pixelXDimension?: int--><!--Device-ExifMetadata-pixelXDimension?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## pixelYDimension

```TypeScript
pixelYDimension?: int
```

Image size on the Y axis (vertical axis in a two-dimensional coordinate system). The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-pixelYDimension?: int--><!--Device-ExifMetadata-pixelYDimension?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## planarConfiguration

```TypeScript
planarConfiguration?: int
```

Whether the pixel components are recorded in chunked or planar format. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-planarConfiguration?: int--><!--Device-ExifMetadata-planarConfiguration?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## primaryChromaticities

```TypeScript
primaryChromaticities?: double[]
```

Chromaticity of the image primaries.

**Type:** double[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-primaryChromaticities?: double[]--><!--Device-ExifMetadata-primaryChromaticities?: double[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## recommendedExposureIndex

```TypeScript
recommendedExposureIndex?: int
```

GPS measurement mode. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-recommendedExposureIndex?: int--><!--Device-ExifMetadata-recommendedExposureIndex?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## referenceBlackWhite

```TypeScript
referenceBlackWhite?: double[]
```

Reference black point value and white point value.

**Type:** double[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-referenceBlackWhite?: double[]--><!--Device-ExifMetadata-referenceBlackWhite?: double[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## relatedSoundFile

```TypeScript
relatedSoundFile?: string
```

Name of the audio file related to the image data.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-relatedSoundFile?: string--><!--Device-ExifMetadata-relatedSoundFile?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## resolutionUnit

```TypeScript
resolutionUnit?: int
```

Unit of the image resolution in the width and height directions. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-resolutionUnit?: int--><!--Device-ExifMetadata-resolutionUnit?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## rowsPerStrip

```TypeScript
rowsPerStrip?: int
```

Number of rows per image strip. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-rowsPerStrip?: int--><!--Device-ExifMetadata-rowsPerStrip?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## samplesPerPixel

```TypeScript
samplesPerPixel?: int
```

Number of color components per pixel, applicable to RGB and YCbCr color models. Since both the models are three-component models (three color channels, or one luminance component plus two chroma components), the standard value for this property is 3. For JPEG-compressed images, this property will be replaced by the corresponding JPEG marker. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-samplesPerPixel?: int--><!--Device-ExifMetadata-samplesPerPixel?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## saturation

```TypeScript
saturation?: int
```

Color saturation adjustment policy applied by the camera. For example, standard processing and saturation reduction. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-saturation?: int--><!--Device-ExifMetadata-saturation?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## sceneCaptureType

```TypeScript
sceneCaptureType?: int
```

Type of the scene that is captured. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-sceneCaptureType?: int--><!--Device-ExifMetadata-sceneCaptureType?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## sceneType

```TypeScript
sceneType?: ArrayBuffer
```

Scene type.

**Type:** ArrayBuffer

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-sceneType?: ArrayBuffer--><!--Device-ExifMetadata-sceneType?: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## sensingMethod

```TypeScript
sensingMethod?: int
```

Type of the image sensor on the camera. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-sensingMethod?: int--><!--Device-ExifMetadata-sensingMethod?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## sensitivityType

```TypeScript
sensitivityType?: int
```

Sensitivity type. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-sensitivityType?: int--><!--Device-ExifMetadata-sensitivityType?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## sharpness

```TypeScript
sharpness?: int
```

Edge enhancement processing method applied by the camera. For example, weak sharpening and standard sharpening. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-sharpness?: int--><!--Device-ExifMetadata-sharpness?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## shutterSpeedValue

```TypeScript
shutterSpeedValue?: double
```

Shutter speed, expressed as an Additive System of Photographic Exposure (APEX) value.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-shutterSpeedValue?: double--><!--Device-ExifMetadata-shutterSpeedValue?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## software

```TypeScript
software?: string
```

Name and version number of the software used to create the image.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-software?: string--><!--Device-ExifMetadata-software?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## sourceExposureTimesOfCompositeImage

```TypeScript
sourceExposureTimesOfCompositeImage?: ArrayBuffer
```

Exposure time of source images for the composite image, for example, 1/33 s.

**Type:** ArrayBuffer

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-sourceExposureTimesOfCompositeImage?: ArrayBuffer--><!--Device-ExifMetadata-sourceExposureTimesOfCompositeImage?: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## sourceImageNumberOfCompositeImage

```TypeScript
sourceImageNumberOfCompositeImage?: int[]
```

Number of source images of the composite image.

**Type:** int[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-sourceImageNumberOfCompositeImage?: int[]--><!--Device-ExifMetadata-sourceImageNumberOfCompositeImage?: int[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## spatialFrequencyResponse

```TypeScript
spatialFrequencyResponse?: ArrayBuffer
```

Spatial frequency table of the camera or input device.

**Type:** ArrayBuffer

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-spatialFrequencyResponse?: ArrayBuffer--><!--Device-ExifMetadata-spatialFrequencyResponse?: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## spectralSensitivity

```TypeScript
spectralSensitivity?: string
```

Spectral sensitivity of each channel of the camera.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-spectralSensitivity?: string--><!--Device-ExifMetadata-spectralSensitivity?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## standardOutputSensitivity

```TypeScript
standardOutputSensitivity?: int
```

Standard output sensitivity. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-standardOutputSensitivity?: int--><!--Device-ExifMetadata-standardOutputSensitivity?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## stripByteCounts

```TypeScript
stripByteCounts?: int[]
```

Number of bytes in each strip after compression.

**Type:** int[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-stripByteCounts?: int[]--><!--Device-ExifMetadata-stripByteCounts?: int[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## stripOffsets

```TypeScript
stripOffsets?: int[]
```

Strip storage offset of the image data, in bytes. To improve the efficiency of large image access, the original pixel data is divided into multiple contiguous blocks (called strips). This property stores the starting offset of each strip in the file sequentially.

**Type:** int[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-stripOffsets?: int[]--><!--Device-ExifMetadata-stripOffsets?: int[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## subfileType

```TypeScript
subfileType?: int
```

Data type of a subfile. It has been deprecated. Use **newSubfileType** instead. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-subfileType?: int--><!--Device-ExifMetadata-subfileType?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## subjectArea

```TypeScript
subjectArea?: int[]
```

Location and area of the main object in the entire scene.

**Type:** int[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-subjectArea?: int[]--><!--Device-ExifMetadata-subjectArea?: int[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## subjectDistance

```TypeScript
subjectDistance?: double
```

Distance from the capture device to the photographed object, in meters.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-subjectDistance?: double--><!--Device-ExifMetadata-subjectDistance?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## subjectDistanceRange

```TypeScript
subjectDistanceRange?: int
```

Distance range to the object. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-subjectDistanceRange?: int--><!--Device-ExifMetadata-subjectDistanceRange?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## subjectLocation

```TypeScript
subjectLocation?: int[]
```

Pixel coordinates of the primary object in the image (based on the origin in the upper left corner).

**Type:** int[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-subjectLocation?: int[]--><!--Device-ExifMetadata-subjectLocation?: int[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## subsecTime

```TypeScript
subsecTime?: string
```

Second fraction of **DateTime**.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-subsecTime?: string--><!--Device-ExifMetadata-subsecTime?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## subsecTimeDigitized

```TypeScript
subsecTimeDigitized?: string
```

Second of **DateTimeDigitized**.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-subsecTimeDigitized?: string--><!--Device-ExifMetadata-subsecTimeDigitized?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## subsecTimeOriginal

```TypeScript
subsecTimeOriginal?: string
```

Second of **DateTimeOriginal**.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-subsecTimeOriginal?: string--><!--Device-ExifMetadata-subsecTimeOriginal?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## transferFunction

```TypeScript
transferFunction?: string
```

Transfer function for the image, which is usually used for color correction.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-transferFunction?: string--><!--Device-ExifMetadata-transferFunction?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## userComment

```TypeScript
userComment?: string
```

User comments.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-userComment?: string--><!--Device-ExifMetadata-userComment?: string-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## whiteBalance

```TypeScript
whiteBalance?: int
```

White balance. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-whiteBalance?: int--><!--Device-ExifMetadata-whiteBalance?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## whitePoint

```TypeScript
whitePoint?: double[]
```

Chromaticity of the image white point.

**Type:** double[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-whitePoint?: double[]--><!--Device-ExifMetadata-whitePoint?: double[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## xResolution

```TypeScript
xResolution?: double
```

Image resolution in the width direction.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-xResolution?: double--><!--Device-ExifMetadata-xResolution?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## yCbCrCoefficients

```TypeScript
yCbCrCoefficients?: double[]
```

Transformation matrix coefficients for converting RGB image data to YCbCr image data.

**Type:** double[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-yCbCrCoefficients?: double[]--><!--Device-ExifMetadata-yCbCrCoefficients?: double[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## yCbCrPositioning

```TypeScript
yCbCrPositioning?: int
```

Position of chroma components relative to the luminance component. The value range is all integers.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-yCbCrPositioning?: int--><!--Device-ExifMetadata-yCbCrPositioning?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## yCbCrSubSampling

```TypeScript
yCbCrSubSampling?: int[]
```

Sampling ratios of the chroma components and luminance component.

**Type:** int[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-yCbCrSubSampling?: int[]--><!--Device-ExifMetadata-yCbCrSubSampling?: int[]-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## yResolution

```TypeScript
yResolution?: double
```

Image resolution in the height direction.

**Type:** double

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExifMetadata-yResolution?: double--><!--Device-ExifMetadata-yResolution?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

