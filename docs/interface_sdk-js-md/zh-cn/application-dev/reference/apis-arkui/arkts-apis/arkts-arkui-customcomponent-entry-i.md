# Entry

Defines Entry Annotation.

Entry is an Annotation and it supports parameters.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export @interface Entry--><!--Device-unnamed-export @interface Entry-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## routeName

```TypeScript
routeName: string = ""
```

Named route name.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Entry-routeName: string = ""--><!--Device-Entry-routeName: string = ""-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## storage

```TypeScript
storage: string = ""
```

Name of the function which returns LocalStorage instance.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Entry-storage: string = ""--><!--Device-Entry-storage: string = ""-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## useSharedStorage

```TypeScript
useSharedStorage: boolean = false
```

Determines whether to use the LocalStorage instance object returned by UIContext.getSharedLocalStorage() interface.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Entry-useSharedStorage: boolean = false--><!--Device-Entry-useSharedStorage: boolean = false-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

