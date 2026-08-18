# TabsController

Defines a tab controller, which is used to control switching of tabs. One **TabsController** cannot control multiple **Tabs** components.

**Since:** 7

<!--Device-unnamed-declare class TabsController--><!--Device-unnamed-declare class TabsController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## changeIndex

```TypeScript
changeIndex(value: number): void
```

Switches to the specified tab.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TabsController-changeIndex(value: number): void--><!--Device-TabsController-changeIndex(value: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **TabsController** object.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TabsController-constructor()--><!--Device-TabsController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## preloadItems

```TypeScript
preloadItems(indices: Optional<Array<number>>): Promise<void>
```

Preloads child nodes. After this API is called, all specified child nodes will be loaded at once. Therefore, for performance considerations, it is recommended that you load child nodes in batches. > **NOTE：**> > - **preloadItems** of **Tabs** needs to be called after **Tabs** is created. You are advised to control the first > preloading in the onAppear lifecycle of **Tabs**. > > - If the **TabsController** object is not bound to any **Tabs** component, a JavaScript exception will be thrown > when this API is called. Therefore, you are advised to use **try-catch** to handle potential exceptions when > calling this API. > > - When using **preloadItems** to preload tabs, you are advised to use **ComponentContent** to customize the > content displayed on the tab bar. For details, see > [Example 10](../../../reference/apis-arkui/arkui-ts/ts-container-tabcontent.md#example-10-setting-tabbar-using-componentcontent).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TabsController-preloadItems(indices: Optional<Array<number>>): Promise<void>--><!--Device-TabsController-preloadItems(indices: Optional<Array<number>>): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [indices](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-customgeometry-c.md) | [Optional](arkts-arkui-optional-t.md)&lt;Array&lt;number&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setTabBarOpacity

```TypeScript
setTabBarOpacity(opacity: number): void
```

Sets the opacity of the tab bar. > **NOTE：**> > When a **Tabs** component is bound to a scrollable container using APIs like > [bindTabsToScrollable](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#bindtabstoscrollable) > or bindTabsToNestedScrollable](../arkts-apis-uicontext-uicontext.md#bindtabstonestedscrollable13), scrolling the > container will trigger the display and hide animations of the tab bar for all **Tabs** components bound to it. In > this case, any **TabBar** opacity set via the **setTabBarOpacity** API will be overridden. Therefore, avoid using > **bindTabsToScrollable**, **bindTabsToNestedScrollable**, and **setTabBarOpacity** simultaneously.

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-TabsController-setTabBarOpacity(opacity: number): void--><!--Device-TabsController-setTabBarOpacity(opacity: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| opacity | number | Yes |

## setTabBarTranslate

```TypeScript
setTabBarTranslate(translate: TranslateOptions): void
```

Sets the translation distance of the tab bar. > **NOTE：**> > When a **Tabs** component is bound to a scrollable container using APIs like > [bindTabsToScrollable](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#bindtabstoscrollable) > or bindTabsToNestedScrollable](../arkts-apis-uicontext-uicontext.md#bindtabstonestedscrollable13), scrolling the > container will trigger the display and hide animations of the tab bar for all **Tabs** components bound to it. In > this case, calling the **setTabBarTranslate** API has no effect. Therefore, avoid using **bindTabsToScrollable**, > **bindTabsToNestedScrollable**, and **setTabBarTranslate** simultaneously.

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-TabsController-setTabBarTranslate(translate: TranslateOptions): void--><!--Device-TabsController-setTabBarTranslate(translate: TranslateOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| translate | [TranslateOptions](../../apis-na/arkts-apis/arkts-na-common-translateoptions-i.md) | Yes |
