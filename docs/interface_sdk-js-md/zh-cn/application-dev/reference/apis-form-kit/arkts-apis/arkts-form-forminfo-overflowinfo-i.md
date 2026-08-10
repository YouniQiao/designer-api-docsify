# OverflowInfo

Provides OverflowInfo about funInteraction or sceneAnimation form

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-formInfo-interface OverflowInfo--><!--Device-formInfo-interface OverflowInfo-End-->

**系统能力：** SystemCapability.Ability.Form

## 导入模块

```TypeScript
import { formInfo } from 'kits/@kit.FormKit';
```

## area

```TypeScript
area: Rect
```

The overflow animation area

**类型：** [Rect](arkts-form-forminfo-rect-i.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-OverflowInfo-area: Rect--><!--Device-OverflowInfo-area: Rect-End-->

**系统能力：** SystemCapability.Ability.Form

## duration

```TypeScript
duration: int
```

The overflow animation duration, unit is ms Unit: milliseconds, The value must be an integer within [0,3500].

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-OverflowInfo-duration: int--><!--Device-OverflowInfo-duration: int-End-->

**系统能力：** SystemCapability.Ability.Form

## useDefaultAnimation

```TypeScript
useDefaultAnimation?: boolean
```

Whether use default animation, default is true

**类型：** boolean

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-OverflowInfo-useDefaultAnimation?: boolean--><!--Device-OverflowInfo-useDefaultAnimation?: boolean-End-->

**系统能力：** SystemCapability.Ability.Form

