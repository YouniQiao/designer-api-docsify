# InputTextMode

Describes the text input mode.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface InputTextMode--><!--Device-unnamed-declare interface InputTextMode-End-->

**System capability:** SystemCapability.Test.UiTest

## addition

```TypeScript
addition?: boolean
```

Whether to input text in addition mode. The value **true** means to input text in addition mode, and **false** means the opposite. Default value: **false**

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-InputTextMode-addition?: boolean--><!--Device-InputTextMode-addition?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

## paste

```TypeScript
paste?: boolean
```

Whether to copy and paste text. The value **true** means to copy and paste text, and **false** means to type text. Default value: **false** **Note**: If the input text contains Chinese characters, special characters, or the text length exceeds 200 characters, the text is copied and pasted regardless of the value of this parameter.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-InputTextMode-paste?: boolean--><!--Device-InputTextMode-paste?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

