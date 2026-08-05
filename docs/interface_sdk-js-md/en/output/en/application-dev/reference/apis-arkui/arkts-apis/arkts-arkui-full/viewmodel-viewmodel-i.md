# ViewModel

ViewModel

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

<!--Device-unnamed-export interface ViewModel--><!--Device-unnamed-export interface ViewModel-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $child

```TypeScript
$child(id: string): ViewModel & object
```

Obtains the ViewModel instance of a custom child component with a specified ID. Usage:this.\$child('xxx'): Obtain the ViewModel instance of a custom child component whose ID is xxx.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$child(id: string): ViewModel & object--><!--Device-ViewModel-$child(id: string): ViewModel & object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | Component ID. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ & object |  |

## $delete

```TypeScript
$delete(key: string): void
```

Deletes an attribute. Usage:this.\$delete('key'): Delete an attribute.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$delete(key: string): void--><!--Device-ViewModel-$delete(key: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes |  |

## $element

```TypeScript
$element(
    id?: string,
  ): AnimationElement &
    CanvasElement &
    object &
    WebElement &
    CameraElement &
    ListElement &
    SwiperElement &
    DialogElement &
    ImageAnimatorElement &
    MarqueeElement &
    MenuElement &
    ChartElement &
    InputElement &
    ButtonElement &
    TextAreaElement &
    PickerElement &
    VideoElement &
    DivElement
```

Obtains the component with a specified ID. If no ID is specified, the root component is returned. Usage: \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ this.\$element('xxx'): Obtain the component whose ID is xxx. this.\$element(): Obtain the root component.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$element(    id?: string,  ): AnimationElement &    CanvasElement &    object &    WebElement &    CameraElement &    ListElement &    SwiperElement &    DialogElement &    ImageAnimatorElement &    MarqueeElement &    MenuElement &    ChartElement &    InputElement &    ButtonElement &    TextAreaElement &    PickerElement &    VideoElement &    DivElement--><!--Device-ViewModel-$element(    id?: string,  ): AnimationElement &    CanvasElement &    object &    WebElement &    CameraElement &    ListElement &    SwiperElement &    DialogElement &    ImageAnimatorElement &    MarqueeElement &    MenuElement &    ChartElement &    InputElement &    ButtonElement &    TextAreaElement &    PickerElement &    VideoElement &    DivElement-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | No | Component ID. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ &     CanvasElement &     object &     WebElement &     CameraElement &     ListElement &     SwiperElement &     DialogElement &     ImageAnimatorElement &     MarqueeElement &     MenuElement &     ChartElement &     InputElement &     ButtonElement &     TextAreaElement &     PickerElement &     VideoElement &     DivElement |  |

## $emit

```TypeScript
$emit(event: string, params?: object): void
```

Custom events.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$emit(event: string, params?: object): void--><!--Device-ViewModel-$emit(event: string, params?: object): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | string | Yes | The name of event. |
| params | object | No | The params of event. |

## $parent

```TypeScript
$parent(): ViewModel & object
```

Obtains the parent ViewModel instance.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$parent(): ViewModel & object--><!--Device-ViewModel-$parent(): ViewModel & object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ & object |  |

## $r

```TypeScript
$r(path: string): string
```

Replace the resource path based on the DPI of the current device: this.\$r('image.tv').

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$r(path: string): string--><!--Device-ViewModel-$r(path: string): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Resource file path. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Content. |

## $root

```TypeScript
$root(): ViewModel & object
```

Obtains the root ViewModel instance.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$root(): ViewModel & object--><!--Device-ViewModel-$root(): ViewModel & object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ & object |  |

## $set

```TypeScript
$set(key: string, value: any): void
```

Adds an attribute or modifies an existing attribute. Usage: this.\$set('key',value): Add an attribute.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$set(key: string, value: any): void--><!--Device-ViewModel-$set(key: string, value: any): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes |  |
| value | any | Yes |  |

## $t

```TypeScript
$t(path: string, params?: object | Array<any>): string
```

Sets the parameters based on the system language, for example, this.\$t('strings.hello').

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$t(path: string, params?: object | Array<any>): string--><!--Device-ViewModel-$t(path: string, params?: object | Array<any>): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path of the language resource key. |
| params | object \| Array&lt;any&gt; | No | Content used to replace placeholders during runtime. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Content. |

## $tc

```TypeScript
$tc(path: string, count: number): string
```

Converse between singular and plural forms based on the system language, for example, this.\$tc('strings.plurals'). NOTE The resource content is distinguished by the following JSON keys: zero, one, two, few, many, and other.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$tc(path: string, count: number): string--><!--Device-ViewModel-$tc(path: string, count: number): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Resource file path. |
| count | number | Yes | Value. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Content. |

## $watch

```TypeScript
$watch(data: string, callback: string): void
```

Listens for attribute changes. If the value of the data attribute changes, the bound event is triggered.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$watch(data: string, callback: string): void--><!--Device-ViewModel-$watch(data: string, callback: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes | Attribute. |
| callback | string | Yes | Function name. |

## scrollTo

```TypeScript
scrollTo(options: ScrollOptions): void
```

Scroll the page to the destination.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-scrollTo(options: ScrollOptions): void--><!--Device-ViewModel-scrollTo(options: ScrollOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The properties of event. |

## $app

```TypeScript
$app: Application
```

Object that is exposed in the app.js file and obtained by this.\$app

**Type:** Application

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$app: Application--><!--Device-ViewModel-$app: Application-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $refs

```TypeScript
$refs: ElementReferences
```

An object that holds all DOM elements and component instances that have been registered with the refs attribute.

**Type:** ElementReferences

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ViewModel-$refs: ElementReferences--><!--Device-ViewModel-$refs: ElementReferences-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

