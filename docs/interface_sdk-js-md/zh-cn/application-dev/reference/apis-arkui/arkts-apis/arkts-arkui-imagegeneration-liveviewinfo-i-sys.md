# LiveViewInfo（系统接口）

Information for LiveView in AI image generation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-imageGeneration-interface LiveViewInfo--><!--Device-imageGeneration-interface LiveViewInfo-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## getLongTermTaskId

```TypeScript
getLongTermTaskId(): int
```

Get the long-term task ID for LiveView.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiveViewInfo-getLongTermTaskId(): int--><!--Device-LiveViewInfo-getLongTermTaskId(): int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | Returns the long-term task ID. |

## getWant

```TypeScript
getWant(): Want
```

Get the Want object for LiveView.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiveViewInfo-getWant(): Want--><!--Device-LiveViewInfo-getWant(): Want-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Returns the Want object. |

## isLiveViewNeeded

```TypeScript
isLiveViewNeeded(): boolean
```

Check whether LiveView is needed.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-LiveViewInfo-isLiveViewNeeded(): boolean--><!--Device-LiveViewInfo-isLiveViewNeeded(): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if LiveView is needed, false otherwise. |

