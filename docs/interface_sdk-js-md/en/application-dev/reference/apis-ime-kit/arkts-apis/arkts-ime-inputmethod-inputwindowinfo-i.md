# InputWindowInfo

输入法软键盘的窗口信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-inputMethod-export interface InputWindowInfo--><!--Device-inputMethod-export interface InputWindowInfo-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## displayId

```TypeScript
displayId?: long
```

输入法软键盘窗口所在的屏幕ID。

**模型约束：** 该参数仅可在Stage模型下使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputWindowInfo-displayId?: long--><!--Device-InputWindowInfo-displayId?: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## height

```TypeScript
height: long
```

输入法窗口的高度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputWindowInfo-height: long--><!--Device-InputWindowInfo-height: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## left

```TypeScript
left: int
```

输入法窗口左上顶点的横坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputWindowInfo-left: int--><!--Device-InputWindowInfo-left: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## name

```TypeScript
name: string
```

输入法窗口的名称。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputWindowInfo-name: string--><!--Device-InputWindowInfo-name: string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## top

```TypeScript
top: int
```

输入法窗口左上顶点的纵坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputWindowInfo-top: int--><!--Device-InputWindowInfo-top: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## width

```TypeScript
width: long
```

输入法窗口的宽度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputWindowInfo-width: long--><!--Device-InputWindowInfo-width: long-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

