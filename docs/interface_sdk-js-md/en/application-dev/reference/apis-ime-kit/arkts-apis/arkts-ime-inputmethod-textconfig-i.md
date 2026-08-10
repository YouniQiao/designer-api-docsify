# TextConfig

编辑框的配置信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-inputMethod-export interface TextConfig--><!--Device-inputMethod-export interface TextConfig-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## capitalizeMode

```TypeScript
capitalizeMode?: CapitalizeMode
```

编辑框设置大小写模式。如果没有设置或设置非法值，默认不进行任何首字母大写处理。

**Type:** [CapitalizeMode](arkts-ime-inputmethod-capitalizemode-e.md)

**Default:** CapitalizeMode.NONE

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-TextConfig-capitalizeMode?: CapitalizeMode--><!--Device-TextConfig-capitalizeMode?: CapitalizeMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## cursorInfo

```TypeScript
cursorInfo?: CursorInfo
```

光标信息。

**Type:** [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-TextConfig-cursorInfo?: CursorInfo--><!--Device-TextConfig-cursorInfo?: CursorInfo-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## inputAttribute

```TypeScript
inputAttribute: InputAttribute
```

编辑框属性。

**Type:** [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-TextConfig-inputAttribute: InputAttribute--><!--Device-TextConfig-inputAttribute: InputAttribute-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## newEditBox

```TypeScript
newEditBox?: boolean
```

表示是否为新编辑框。true表示新编辑框，false表示非新编辑框。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-TextConfig-newEditBox?: boolean--><!--Device-TextConfig-newEditBox?: boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## selection

```TypeScript
selection?: Range
```

文本选中的范围。

**Type:** [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-TextConfig-selection?: Range--><!--Device-TextConfig-selection?: Range-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## windowId

```TypeScript
windowId?: int
```

编辑框所在的窗口Id，该参数应为整数。

推荐使用[getWindowProperties](../../apis-arkui/arkts-apis/arkts-arkui-window-window-i.md/arkts-arkui-window-window-i.md#getwindowproperties)方法获取窗口id属性。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-TextConfig-windowId?: int--><!--Device-TextConfig-windowId?: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

