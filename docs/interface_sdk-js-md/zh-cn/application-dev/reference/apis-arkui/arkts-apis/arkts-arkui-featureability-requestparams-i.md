# RequestParams

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-unnamed-export interface RequestParams--><!--Device-unnamed-export interface RequestParams-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## abilityName

```TypeScript
abilityName?: string
```

Ability name, which is case sensitive.

**类型：** string

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-RequestParams-abilityName?: string--><!--Device-RequestParams-abilityName?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## action

```TypeScript
action?: string
```

Without specifying the bundle name and ability name, you can start the application according to other properties with action.

**类型：** string

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-RequestParams-action?: string--><!--Device-RequestParams-action?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## bundleName

```TypeScript
bundleName?: string
```

The name of the bundle to start. It should be used with abilityname and case sensitive.

**类型：** string

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-RequestParams-bundleName?: string--><!--Device-RequestParams-bundleName?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## data

```TypeScript
data?: object
```

Data sent to the ability which need to be serializable.

**类型：** object

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-RequestParams-data?: object--><!--Device-RequestParams-data?: object-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## deviceType

```TypeScript
deviceType?: number
```

If more than one FA meets the conditions, the user can select the device from the popup.0: Default. Select the FA to start from the local and remote devices.1: start FA from the local device.

**类型：** number

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-RequestParams-deviceType?: number--><!--Device-RequestParams-deviceType?: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## entities

```TypeScript
entities?: Array<string>
```

The list of entities to which the FA to be called. If it is not filled in, all entity lists will be found by default. It should be used with action.

**类型：** Array&lt;string&gt;

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-RequestParams-entities?: Array<string>--><!--Device-RequestParams-entities?: Array<string>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## flag

```TypeScript
flag?: number
```

Configuration switch when start FA.

**类型：** number

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-RequestParams-flag?: number--><!--Device-RequestParams-flag?: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## url

```TypeScript
url?: string
```

Specify the url of the page which the FA to be called. Use home page directly by default.

**类型：** string

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-RequestParams-url?: string--><!--Device-RequestParams-url?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

