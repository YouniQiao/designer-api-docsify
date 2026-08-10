# PersistPropsOptions

用于指定持久化属性及其默认值的键值对对象，作为[persistProps](arkts-arkui-persistentstorage-c.md#persistprops)参数传入。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface PersistPropsOptions--><!--Device-unnamed-declare interface PersistPropsOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultValue

```TypeScript
defaultValue: number | string | boolean | Object
```

在PersistentStorage和AppStorage中未查询到时，则使用默认值进行初始化。从API version 12开始，defaultValue可以为null或undefined。

**Type:** number \| string \| boolean \| Object

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PersistPropsOptions-defaultValue: number | string | boolean | Object--><!--Device-PersistPropsOptions-defaultValue: number | string | boolean | Object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key: string
```

要持久化的属性名。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PersistPropsOptions-key: string--><!--Device-PersistPropsOptions-key: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

