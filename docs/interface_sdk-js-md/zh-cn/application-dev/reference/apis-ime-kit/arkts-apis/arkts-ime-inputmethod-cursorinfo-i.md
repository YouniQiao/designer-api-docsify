# CursorInfo

光标信息。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## displayId

```TypeScript
displayId?: long
```

光标所在显示器的ID，该参数应为整数，最小值为0，默认值为0。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**默认值：** 0

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## height

```TypeScript
height: double
```

光标的高度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## left

```TypeScript
left: double
```

光标的横坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## top

```TypeScript
top: double
```

光标的纵坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## width

```TypeScript
width: double
```

光标的宽度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework
