# TextMenuItemId

Defines the TextMenuItemId.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## equals

```TypeScript
equals(id: TextMenuItemId): boolean
```

Judge if two TextMenuItemId are equal.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## of

```TypeScript
static of(id: ResourceStr): TextMenuItemId
```

Init a TextMenuItemId with id.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md) |

## address

```TypeScript
static readonly address: TextMenuItemId
```

Indicates the TextMenuItemId to open map.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AI_WRITER

```TypeScript
static readonly AI_WRITER: TextMenuItemId
```

Indicates the TextMenuItemId to help with text creation by invoking large models.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## askAI

```TypeScript
static readonly askAI: TextMenuItemId
```

Indicates the TextMenuItemId for asking AI.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoFill

```TypeScript
static readonly autoFill: TextMenuItemId
```

Indicates the TextMenuItemId for auto fill.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CAMERA_INPUT

```TypeScript
static readonly CAMERA_INPUT: TextMenuItemId
```

Indicates the TextMenuItemId to recognize the text in the picture and input it into the text view.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## COLLABORATION_SERVICE

```TypeScript
static readonly COLLABORATION_SERVICE: TextMenuItemId
```

Indicates the TextMenuItemId for collaboration service menu items.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## COPY

```TypeScript
static readonly COPY: TextMenuItemId
```

Indicates the TextMenuItemId to copy the currently selected text to the clipboard.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CUT

```TypeScript
static readonly CUT: TextMenuItemId
```

Indicates the TextMenuItemId to copy and delete the currently selected text.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dateTime

```TypeScript
static readonly dateTime: TextMenuItemId
```

Indicates the TextMenuItemId to open calendar.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## email

```TypeScript
static readonly email: TextMenuItemId
```

Indicates the TextMenuItemId to open email.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## passwordVault

```TypeScript
static readonly passwordVault: TextMenuItemId
```

Indicates the TextMenuItemId for password vault.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PASTE

```TypeScript
static readonly PASTE: TextMenuItemId
```

Indicates the TextMenuItemId to copy the current contents of the clipboard into the text view.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## phoneNumber

```TypeScript
static readonly phoneNumber: TextMenuItemId
```

Indicates the TextMenuItemId to call the phone number.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SEARCH

```TypeScript
static readonly SEARCH: TextMenuItemId
```

Indicates the TextMenuItemId to search the selected content.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SELECT_ALL

```TypeScript
static readonly SELECT_ALL: TextMenuItemId
```

Indicates the TextMenuItemId to select all text in a text view.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SHARE

```TypeScript
static readonly SHARE: TextMenuItemId
```

Indicates the TextMenuItemId to share the selected content.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TRANSLATE

```TypeScript
static readonly TRANSLATE: TextMenuItemId
```

Indicates the TextMenuItemId to translate the selected content.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## url

```TypeScript
static readonly url: TextMenuItemId
```

Indicates the TextMenuItemId to open url.

**Type:** [TextMenuItemId](arkts-arkui-textcommon-textmenuitemid-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
