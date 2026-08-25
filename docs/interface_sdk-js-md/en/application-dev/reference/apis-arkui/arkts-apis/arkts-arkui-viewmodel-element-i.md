# Element

Element@interface Element

**Since:** 4

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addChild

```TypeScript
addChild(child: Element): void
```

Adds a node to the end of the child node list of the current node.

**Since:** 8

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [child](../arkts-components/arkts-arkui-nestedscrollinfo-i.md) | [Element](arkts-arkui-viewmodel-element-i.md) | Yes |

## animate

```TypeScript
animate(keyframes: Array<AnimateStyle>, options: AnimateOptions): AnimationResult
```

Creates and runs an animation shortcut on the component. Specify the keyframes and options required for the animation.

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyframes | Array&lt;[AnimateStyle](arkts-arkui-viewmodel-animatestyle-i.md)&gt; | Yes |
| options | [AnimateOptions](arkts-arkui-viewmodel-animateoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AnimationResult](arkts-arkui-viewmodel-animationresult-i.md) |

## createIntersectionObserver

```TypeScript
createIntersectionObserver(param: { ratios: Array<number> }): observer
```

If 0.5 is returned, 50% of the current component is visible.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | { ratios: Array & lt;number & gt; } | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [observer](arkts-arkui-viewmodel-observer-i.md) |

## focus

```TypeScript
focus(obj?: FocusParamObj): void
```

Requests or cancels the focus for a component. If focus is set to true, the focus is requested for the component. If focus is set to false, the focus is canceled for the component. This attribute can be defaulted to true.

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | [FocusParamObj](arkts-arkui-viewmodel-focusparamobj-i.md) | No | { focus: true \|

## getBoundingClientRect

```TypeScript
getBoundingClientRect(): RectObj
```

Obtains the size and position of the element.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RectObj](arkts-arkui-viewmodel-rectobj-i.md) |

## rotation

```TypeScript
rotation(obj?: FocusParamObj): void
```

Requests or cancels the crown rotation focus for a component. If focus is set to true, the crown event focus is requested. If focus is set to false, the crown event focus is canceled. This attribute can be defaulted to true.

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | [FocusParamObj](arkts-arkui-viewmodel-focusparamobj-i.md) | No | { focus: true \|

## setAttribute

```TypeScript
setAttribute(name: string, value: string): void
```

Sets the value of an attribute on a specified element. If the attribute already exists, update the value. Otherwise, a new attribute is added with the specified name and value.

**Since:** 8

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| value | string | Yes |

## setStyle

```TypeScript
setStyle(name: string, value: string): boolean
```

Sets a style value on a specified element. If the style exists and the style value is valid, the setting is successful. Otherwise, the setting is invalid.

**Since:** 8

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
