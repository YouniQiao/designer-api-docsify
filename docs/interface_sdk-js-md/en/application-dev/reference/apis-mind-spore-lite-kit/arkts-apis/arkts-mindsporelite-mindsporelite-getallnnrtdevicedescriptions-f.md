# getAllNNRTDeviceDescriptions

## Modules to Import

```TypeScript
import { mindSporeLite } from '@kit.MindSporeLiteKit';
```

## getAllNNRTDeviceDescriptions

```TypeScript
function getAllNNRTDeviceDescriptions() : NNRTDeviceDescription[]
```

Obtain the all device descriptions in NNRT.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function getAllNNRTDeviceDescriptions() : NNRTDeviceDescription[]--><!--Device-mindSporeLite-function getAllNNRTDeviceDescriptions() : NNRTDeviceDescription[]-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Return value:**

| Type | Description |
| --- | --- |
| [NNRTDeviceDescription](arkts-mindsporelite-mindsporelite-nnrtdevicedescription-i.md)[] | the array of NNRTDeviceDescription |

## Examples

```TypeScript
let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
if (allDevices == null) {
  console.error('MS_LITE_LOG: getAllNNRTDeviceDescriptions is NULL.');
}
```

