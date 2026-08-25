# TabsSidebarSearchableOptions

Defines the options for the searchable sidebar tab bar.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## searchCallback

```TypeScript
searchCallback?: (text: string) => void
```

Callback triggered when the search text changes.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

## searchFilter

```TypeScript
searchFilter?: TabsSidebarSearchFilterCallback
```

Filter function to determine whether a tab should be displayed based on the search text.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placeholder

```TypeScript
placeholder?: ResourceStr
```

Placeholder text displayed when the search input is empty.

**Type:** ResourceStr

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## searchText

```TypeScript
searchText?: ResourceStr
```

Sets the text input in the search text box.

**Type:** ResourceStr

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
