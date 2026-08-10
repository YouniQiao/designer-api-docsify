# ViewModel

View model

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

<!--Device-unnamed-export interface ViewModel--><!--Device-unnamed-export interface ViewModel-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## $t

```TypeScript
$t(path: string, param?: object | Array<any>): string
```

Displays content based on the current system language and a path of the language resource key specified through \$t.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ViewModel-$t(path: string, param?: object | Array<any>): string--><!--Device-ViewModel-$t(path: string, param?: object | Array<any>): string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | Path of the language resource key |
| param | object \| Array&lt;any&gt; | 否 | Content used to replace placeholders during runtime. There are two types of placeholders available: 1. Named placeholder, for example, {name}. The actual content must be of the object type, for example, \\$t('strings.object', {name: 'Hello world'}). 2. Digit placeholder, for example, {0}. The actual content must be of the array type, for example, \\$t('strings.array', ['Hello world']). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | content to display |

## $refs

```TypeScript
$refs: ElementReferences
```

An object that holds all DOM elements and component instances that have been registered with the refs attribute

**类型：** [ElementReferences](arkts-arkui-viewmodel-elementreferences-i.md)

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ViewModel-$refs: ElementReferences--><!--Device-ViewModel-$refs: ElementReferences-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

