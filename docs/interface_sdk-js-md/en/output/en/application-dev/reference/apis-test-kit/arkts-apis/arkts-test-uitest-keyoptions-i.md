# KeyOptions

Represents the options for key operations.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-declare interface KeyOptions--><!--Device-unnamed-declare interface KeyOptions-End-->

**System capability:** SystemCapability.Test.UiTest

## key1

```TypeScript
key1?: int
```

The first keyCode to press during the operation. If not set, no key event will be injected. Setting only key2 without key1 will result in a BusinessError 17000007.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-KeyOptions-key1?: int--><!--Device-KeyOptions-key1?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## key2

```TypeScript
key2?: int
```

The second KeyCode to press during the operation. If not set, no key event will be injected. Setting only key2 without key1 will result in a BusinessError 17000007.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-KeyOptions-key2?: int--><!--Device-KeyOptions-key2?: int-End-->

**System capability:** SystemCapability.Test.UiTest

