# NNRTDevice

Provides the NNRT device info

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-mindSporeLite-interface NNRTDevice--><!--Device-mindSporeLite-interface NNRTDevice-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## 导入模块

```TypeScript
import { mindSporeLite } from 'kits/@kit.MindSporeLiteKit';
```

## deviceID

```TypeScript
deviceID?: bigint
```

NNRT device id.

**类型：** bigint

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NNRTDevice-deviceID?: bigint--><!--Device-NNRTDevice-deviceID?: bigint-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## extensions

```TypeScript
extensions?: Extension[]
```

NNRT device extension array.

**类型：** [Extension](arkts-mindsporelite-mindsporelite-extension-i.md)[]

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NNRTDevice-extensions?: Extension[]--><!--Device-NNRTDevice-extensions?: Extension[]-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## performanceMode

```TypeScript
performanceMode?: PerformanceMode
```

NNRT device performance mode.

**类型：** [PerformanceMode](arkts-mindsporelite-mindsporelite-performancemode-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NNRTDevice-performanceMode?: PerformanceMode--><!--Device-NNRTDevice-performanceMode?: PerformanceMode-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

## priority

```TypeScript
priority?: Priority
```

NNRT device priority.

**类型：** [Priority](../../apis-arkts/arkts-apis/arkts-arkts-taskpool-priority-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NNRTDevice-priority?: Priority--><!--Device-NNRTDevice-priority?: Priority-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

