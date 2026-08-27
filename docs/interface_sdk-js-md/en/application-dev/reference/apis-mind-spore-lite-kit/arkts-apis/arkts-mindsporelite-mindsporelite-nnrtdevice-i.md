# NNRTDevice

Provides the NNRT device info

**Since:** 10

**System capability:** SystemCapability.AI.MindSporeLite

## Modules to Import

```TypeScript
import { mindSporeLite } from '@kit.MindSporeLiteKit';
```

## deviceID

```TypeScript
deviceID?: bigint
```

NNRT device id.

**Type:** bigint

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Examples**

```TypeScript
let context: mindSporeLite.Context = {};
context.target = ["nnrt"];
context.nnrt = {};
let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
if (allDevices == null || allDevices.length === 0) {
  console.error(`Failed to get NNRT device descriptions. Context: ${JSON.stringify(context)}, Result: null or empty`);
} else {
  console.info(`Succeeded in getting NNRT device descriptions. Device count: ${allDevices.length}`);
    for (let i: number = 0; i < allDevices.length; i++) {
      console.info(`Device ${i} ID: ${allDevices[i].deviceID().toString()}`);
  }
}
```

## extensions

```TypeScript
extensions?: Extension[]
```

NNRT device extension array.

**Type:** [Extension](arkts-mindsporelite-mindsporelite-extension-i.md)[]

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

## performanceMode

```TypeScript
performanceMode?: PerformanceMode
```

NNRT device performance mode.

**Type:** [PerformanceMode](arkts-mindsporelite-mindsporelite-performancemode-e.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

## priority

```TypeScript
priority?: Priority
```

NNRT device priority.

**Type:** Priority

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite
