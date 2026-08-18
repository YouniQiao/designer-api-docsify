# back

## Modules to Import

```TypeScript
```

## back

```TypeScript
function back(options?: RouterOptions): void
```

Returns to the previous page or a specified page, which deletes all pages between the current page and the target page. > **NOTE：**> > - Since API version 10, you can use the > [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#uicontext) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md#uicontext) object associated > with the current UI context.

**Since:** 8

**Deprecated since:** 18

**Substitutes:** [back](arkts-arkui-arkui-uicontext-router-c.md#back)(options?: router.RouterOptions)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function back(options?: RouterOptions): void--><!--Device-router-function back(options?: RouterOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | No |

**Examples**

```TypeScript
this.getUIContext().getRouter().back({ url: 'pages/detail' });
```


## back

```TypeScript
function back(index: number, params?: Object): void
```

Returns to the specified page, which deletes all pages between the current page and the target page. > **NOTE：**> > - Since API version 12, you can use the > [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#uicontext) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md#uicontext) object associated > with the current UI context.

**Since:** 12

**Deprecated since:** 18

**Substitutes:** [back](arkts-arkui-arkui-uicontext-router-c.md#back)(index: number, params?: Object)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-router-function back(index: number, params?: Object): void--><!--Device-router-function back(index: number, params?: Object): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| params | Object | No |

**Examples**

```TypeScript
this.getUIContext().getRouter().back(1);
```

```TypeScript
this.getUIContext().getRouter().back(1, { info: 'From Home' }); // Returning with parameters.
```
