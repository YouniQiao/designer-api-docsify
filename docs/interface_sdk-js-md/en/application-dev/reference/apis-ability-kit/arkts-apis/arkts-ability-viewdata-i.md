# ViewData

The module defines the view data used for auto-fill.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-export default interface ViewData--><!--Device-unnamed-export default interface ViewData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## abilityName

```TypeScript
abilityName: string
```

Ability name.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ViewData-abilityName: string--><!--Device-ViewData-abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## bundleName

```TypeScript
bundleName: string
```

Bundle name.The value cannot exceed 512 characters.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ViewData-bundleName: string--><!--Device-ViewData-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## isOtherAccount

```TypeScript
isOtherAccount: boolean
```

Whether to display other account information saved in the password box for the user to select. **true** to display,  
**false** otherwise.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ViewData-isOtherAccount: boolean--><!--Device-ViewData-isOtherAccount: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## isUserSelected

```TypeScript
isUserSelected: boolean
```

Whether the content to be filled is selected by the user. **true** if the content is selected by the user, and  
**false** otherwise.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ViewData-isUserSelected: boolean--><!--Device-ViewData-isUserSelected: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## moduleName

```TypeScript
moduleName: string
```

Module name.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ViewData-moduleName: string--><!--Device-ViewData-moduleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## pageNodeInfos

```TypeScript
pageNodeInfos: Array<PageNodeInfo>
```

Page node information.

**Type:** Array&lt;[PageNodeInfo](arkts-ability-pagenodeinfo-i.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ViewData-pageNodeInfos: Array<PageNodeInfo>--><!--Device-ViewData-pageNodeInfos: Array<PageNodeInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## pageRect

```TypeScript
pageRect: AutoFillRect
```

Coordinates, width, and height of the page.

**Type:** [AutoFillRect](arkts-ability-autofillrect-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ViewData-pageRect: AutoFillRect--><!--Device-ViewData-pageRect: AutoFillRect-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## pageUrl

```TypeScript
pageUrl: string
```

URL of the page.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ViewData-pageUrl: string--><!--Device-ViewData-pageUrl: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

