# TextResponseType

选择菜单的响应类型。

> **说明：**
> 
> 菜单类型的匹配顺序如下。例如，用户长按文本时，根据以下规则查找：
> 
> 1. 查找是否注册了TextSpanType.TEXT、TextResponseType.LONG_PRESS菜单
> 
> 2. 查找是否注册了TextSpanType.TEXT、TextResponseType.DEFAULT菜单
> 
> 3. 查找是否注册了TextSpanType.DEFAULT、TextResponseType.LONG_PRESS菜单
> 
> 4. 查找是否注册了TextSpanType.DEFAULT、TextResponseType.DEFAULT菜单

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare enum TextResponseType--><!--Device-unnamed-declare enum TextResponseType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RIGHT_CLICK

```TypeScript
RIGHT_CLICK = 0
```

通过鼠标右键触发菜单弹出。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextResponseType-RIGHT_CLICK = 0--><!--Device-TextResponseType-RIGHT_CLICK = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LONG_PRESS

```TypeScript
LONG_PRESS = 1
```

通过长按触发菜单弹出。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextResponseType-LONG_PRESS = 1--><!--Device-TextResponseType-LONG_PRESS = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SELECT

```TypeScript
SELECT = 2
```

通过鼠标选中触发菜单弹出。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextResponseType-SELECT = 2--><!--Device-TextResponseType-SELECT = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 3
```

注册此类型的菜单，但未注册RIGHT_CLICK、LONG_PRESS、SELECT时，右键、长按、鼠标、[selection](TextAttribute#selection)选中均会触发并显示此类型对应的菜单。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-TextResponseType-DEFAULT = 3--><!--Device-TextResponseType-DEFAULT = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

