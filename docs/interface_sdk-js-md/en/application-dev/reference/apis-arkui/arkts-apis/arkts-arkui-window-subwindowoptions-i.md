# SubWindowOptions

子窗口创建参数。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-window-interface SubWindowOptions--><!--Device-window-interface SubWindowOptions-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## decorEnabled

```TypeScript
decorEnabled: boolean
```

子窗口是否显示装饰。true表示子窗口显示装饰，false表示子窗口不显示装饰。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SubWindowOptions-decorEnabled: boolean--><!--Device-SubWindowOptions-decorEnabled: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## isModal

```TypeScript
isModal?: boolean
```

子窗口是否启用模态属性。true表示子窗口启用模态属性，false表示子窗口禁用模态属性。不设置，则默认为false。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SubWindowOptions-isModal?: boolean--><!--Device-SubWindowOptions-isModal?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## maximizeSupported

```TypeScript
maximizeSupported?: boolean
```

子窗口是否支持最大化特性。true表示子窗口支持最大化，false表示子窗口不支持最大化。不设置，则默认为false。

该参数在支持并处于[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态的设备上可正常调用；在不支持  
[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态的设备上，作为入参使用时，对应接口不生效不报错；在支持但不处于  
[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态的设备上，作为入参使用时，对应接口不生效不报错，切换到  
[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态后生效。

**Type:** boolean

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-SubWindowOptions-maximizeSupported?: boolean--><!--Device-SubWindowOptions-maximizeSupported?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## modalityType

```TypeScript
modalityType?: ModalityType
```

子窗口模态类型，仅当子窗口启用模态属性时生效。不设置，则默认为WINDOW_MODALITY。

**Type:** [ModalityType](arkts-arkui-window-modalitytype-e.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-SubWindowOptions-modalityType?: ModalityType--><!--Device-SubWindowOptions-modalityType?: ModalityType-End-->

**System capability:** SystemCapability.Window.SessionManager

## outlineEnabled

```TypeScript
outlineEnabled?: boolean
```

子窗口是否显示描边。true表示子窗口显示描边，false表示子窗口不显示描边。不设置，则默认为false。

该参数在2in1设备、其他设备的电脑模式中可正常调用，在其他设备和其他模式中作为入参使用时，对应接口不生效不报错。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SubWindowOptions-outlineEnabled?: boolean--><!--Device-SubWindowOptions-outlineEnabled?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## title

```TypeScript
title: string
```

子窗口标题。标题显示区域最右端不超过系统三键区域最左端，超过部分以省略号表示。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SubWindowOptions-title: string--><!--Device-SubWindowOptions-title: string-End-->

**System capability:** SystemCapability.Window.SessionManager

## windowRect

```TypeScript
windowRect?: Rect
```

子窗口矩形区域，其中子窗口存在大小限制，具体参考  
[resize()](arkts-arkui-window-window-i.md#resize)方法。不设置且未调用[showWindow()](arkts-arkui-window-window-i.md#showwindow)显示前，则默认为{left: 0, top: 0, width: 0, height: 0}。具体参考[设置应用子窗口](../../../windowmanager/application-window-stage.md#设置应用子窗口)开发指南。

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubWindowOptions-windowRect?: Rect--><!--Device-SubWindowOptions-windowRect?: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

## zLevel

```TypeScript
zLevel?: int
```

子窗口层级级别，仅当子窗口未启用模态属性，即未设置isModal时生效。该参数是整数，取值范围为[-10000, 10000]，浮点数输入将向下取整。不设置，则默认为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubWindowOptions-zLevel?: int--><!--Device-SubWindowOptions-zLevel?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## zLevelAboveParentLoosened

```TypeScript
zLevelAboveParentLoosened?: boolean
```

标识解除子窗在父窗口的层级限制

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SubWindowOptions-zLevelAboveParentLoosened?: boolean--><!--Device-SubWindowOptions-zLevelAboveParentLoosened?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

