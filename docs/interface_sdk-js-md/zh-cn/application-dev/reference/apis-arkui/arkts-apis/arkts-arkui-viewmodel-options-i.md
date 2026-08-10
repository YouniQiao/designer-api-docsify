# Options

Options type

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

<!--Device-unnamed-export interface Options<T extends ViewModel, Data = DefaultData<T>>--><!--Device-unnamed-export interface Options<T extends ViewModel, Data = DefaultData<T>>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## onCreate

```TypeScript
onCreate?(): void
```

Called when the application is created

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Options-onCreate?(): void--><!--Device-Options-onCreate?(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## onDestroy

```TypeScript
onDestroy?(): void
```

Called when the application is destroyed or called when the page is redirected to another one (without entering the navigation stack).

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Options-onDestroy?(): void--><!--Device-Options-onDestroy?(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## onHide

```TypeScript
onHide?(): void
```

Listens for page hiding.Called when the page disappears.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Options-onHide?(): void--><!--Device-Options-onHide?(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## onInit

```TypeScript
onInit?(): void
```

Called when the page is initialized. This function can be called only once in a lifecycle.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Options-onInit?(): void--><!--Device-Options-onInit?(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## onReady

```TypeScript
onReady?(): void
```

Called when the page is created. This function can be called only once in a lifecycle.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Options-onReady?(): void--><!--Device-Options-onReady?(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## onRestoreData

```TypeScript
onRestoreData?(data: Object): void
```

Called when the user data need to be restored

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Options-onRestoreData?(data: Object): void--><!--Device-Options-onRestoreData?(data: Object): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Object | 是 | Indicates the user data to restore. |

## onSaveData

```TypeScript
onSaveData?(data: Object): boolean
```

Called when the user data need to be saved

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Options-onSaveData?(data: Object): boolean--><!--Device-Options-onSaveData?(data: Object): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Object | 是 | Indicates the user data to save. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

## onShow

```TypeScript
onShow?(): void
```

Called when the page is displayed.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Options-onShow?(): void--><!--Device-Options-onShow?(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## data

```TypeScript
data?: Data
```

Data model of the page that can be converted into a JSON object.The attribute name cannot start with \$ or an underscore (_) or contain the reserved words such as for, if, show, and tid.For a function, the return value must be an object.Set the value of data to the return value of the function during page initialization.

**类型：** Data

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Options-data?: Data--><!--Device-Options-data?: Data-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

