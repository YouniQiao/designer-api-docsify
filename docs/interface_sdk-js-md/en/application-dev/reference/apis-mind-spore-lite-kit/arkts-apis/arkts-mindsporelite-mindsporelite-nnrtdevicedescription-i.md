# NNRTDeviceDescription

Provides the nnrt device description

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-mindSporeLite-interface NNRTDeviceDescription--><!--Device-mindSporeLite-interface NNRTDeviceDescription-End-->

**System capability:** SystemCapability.AI.MindSporeLite

## Modules to Import

```TypeScript
import { mindSporeLite } from '@kit.MindSporeLiteKit';
```

## deviceID

```TypeScript
deviceID() : bigint
```

Get device id

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NNRTDeviceDescription-deviceID() : bigint--><!--Device-NNRTDeviceDescription-deviceID() : bigint-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Return value:**

| Type | Description |
| --- | --- |
| bigint | the number of device id |

## Examples

```TypeScript
let context: mindSporeLite.Context = {};
context.target = ["nnrt"];
context.nnrt = {};
let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
if (allDevices == null) {
  console.error('getAllNNRTDeviceDescriptions is NULL.');
} else {
  for (let i: number = 0; i < allDevices.length; i++) {
    console.info(allDevices[i].deviceID().toString());
  }
}
```

## deviceName

```TypeScript
deviceName() : string
```

Get device name.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NNRTDeviceDescription-deviceName() : string--><!--Device-NNRTDeviceDescription-deviceName() : string-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Return value:**

| Type | Description |
| --- | --- |
| string | device name |

## Examples

```TypeScript
let context: mindSporeLite.Context = {};
context.target = ["nnrt"];
context.nnrt = {};
let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
if (allDevices == null) {
  console.error('getAllNNRTDeviceDescriptions is NULL.');
} else {
  for (let i: number = 0; i < allDevices.length; i++) {
    console.info(allDevices[i].deviceName().toString());
  }
}
```

## deviceType

```TypeScript
deviceType() : NNRTDeviceType
```

Get device type.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NNRTDeviceDescription-deviceType() : NNRTDeviceType--><!--Device-NNRTDeviceDescription-deviceType() : NNRTDeviceType-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Return value:**

| Type | Description |
| --- | --- |
| [NNRTDeviceType](arkts-mindsporelite-mindsporelite-nnrtdevicetype-e.md) | the device type |

## Examples

```TypeScript
let context: mindSporeLite.Context = {};
context.target = ["nnrt"];
context.nnrt = {};
let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
if (allDevices == null) {
  console.error('getAllNNRTDeviceDescriptions is NULL.');
} else {
  for (let i: number = 0; i < allDevices.length; i++) {
    console.info(allDevices[i].deviceType().toString());
  }
}
```

