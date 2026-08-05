# WindowFilter

Provides the flag attributes of this window.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface WindowFilter--><!--Device-unnamed-declare interface WindowFilter-End-->

**System capability:** SystemCapability.Test.UiTest

## active

```TypeScript
active?: boolean
```

Whether the window is interacting with the user. The value **true** indicates that the window is interacting with the user, and **false** indicates the opposite.

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowFilter-active?: boolean--><!--Device-WindowFilter-active?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

## actived

```TypeScript
actived?: boolean
```

Whether the window is interacting with the user. The value **true** indicates that the window is interacting with the user, and **false** indicates the opposite. This API is deprecated since API version 11. You are advised to use the **active** API instead.

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

**Substitutes:** ohos.UiTest.WindowFilter#active

<!--Device-WindowFilter-actived?: boolean--><!--Device-WindowFilter-actived?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

## bundleName

```TypeScript
bundleName?: string
```

Bundle name of the application to which the window belongs. The default value is empty.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowFilter-bundleName?: string--><!--Device-WindowFilter-bundleName?: string-End-->

**System capability:** SystemCapability.Test.UiTest

## displayId

```TypeScript
displayId?: int
```

ID of the display to which the window belongs. The value is an integer greater than or equal to 0. The default value is the default screen ID of the device.

**Type:** int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-WindowFilter-displayId?: int--><!--Device-WindowFilter-displayId?: int-End-->

**System capability:** SystemCapability.Test.UiTest

## focused

```TypeScript
focused?: boolean
```

Whether the window is focused. The value **true** indicates that the window is focused, and **false** indicates the opposite. The default value is **false**.

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowFilter-focused?: boolean--><!--Device-WindowFilter-focused?: boolean-End-->

**System capability:** SystemCapability.Test.UiTest

## title

```TypeScript
title?: string
```

Title of the window. The default value is empty.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowFilter-title?: string--><!--Device-WindowFilter-title?: string-End-->

**System capability:** SystemCapability.Test.UiTest

