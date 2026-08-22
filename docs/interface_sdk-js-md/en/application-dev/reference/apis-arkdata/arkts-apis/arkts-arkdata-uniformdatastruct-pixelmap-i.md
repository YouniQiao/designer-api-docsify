# PixelMap

Represents data of the pixel map type defined by the system.

**Since:** 23

<!--Device-uniformDataStruct-interface PixelMap--><!--Device-uniformDataStruct-interface PixelMap-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { uniformDataStruct } from '@kit.ArkData';
```

## details

```TypeScript
details?: Record<string, int | long | double | string | Uint8Array>
```

Object of the dictionary type used to describe the icon. The key is of the string type, and the value can be a number, a string, or a Uint8Array. By default, it is an empty dictionary object.

**Type:** Record&lt;string, int \| long \| double \| string \| Uint8Array&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-PixelMap-details?: Record<string, int | long | double | string | Uint8Array>--><!--Device-PixelMap-details?: Record<string, int | long | double | string | Uint8Array>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## pixelMap

```TypeScript
pixelMap: image.PixelMap
```

Binary data of the pixel map.

**Type:** image.PixelMap

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-PixelMap-pixelMap: image.PixelMap--><!--Device-PixelMap-pixelMap: image.PixelMap-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uniformDataType

```TypeScript
readonly uniformDataType: 'openharmony.pixel-map'
```

Uniform data type, which has a fixed value of **openharmony.pixel-map**. For details, see [UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md).

**Type:** 'openharmony.pixel-map'

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-PixelMap-readonly uniformDataType: 'openharmony.pixel-map'--><!--Device-PixelMap-readonly uniformDataType: 'openharmony.pixel-map'-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Examples**

```TypeScript
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
import { image } from '@kit.ImageKit';

let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
let arrayBuffer = new ArrayBuffer(4*200*200);
let opt : image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 }, alphaType: 3 };
let pixelMapDetails : Record<string, number | string | Uint8Array> = {
  'pixelMapKey1': 123,
  'pixelMapKey2': 'pixelMapValue',
  'pixelMapKey3': u8Array
}
let pixelMap : uniformDataStruct.PixelMap = {
  uniformDataType : 'openharmony.pixel-map',
  pixelMap : image.createPixelMapSync(arrayBuffer, opt),
  details : pixelMapDetails
}
console.info('pixelMap.uniformDataType: ' + pixelMap.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP, pixelMap);
```

