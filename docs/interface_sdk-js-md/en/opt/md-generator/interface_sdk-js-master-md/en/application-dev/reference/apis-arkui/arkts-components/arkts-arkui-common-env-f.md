# Env

## Modules to Import

```TypeScript
```

## Env

```TypeScript
declare function Env<T>(key: SystemEnvKey<T> | SystemProperties): PropertyDecorator
```

Defining Env PropertyDecorator. On API 26.0.0 and above, the parameter also supports the SystemEnvKey&lt;T&gt; type.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-unnamed-declare function Env<T>(key: SystemEnvKey<T> | SystemProperties): PropertyDecorator--><!--Device-unnamed-declare function Env<T>(key: SystemEnvKey<T> | SystemProperties): PropertyDecorator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [SystemEnvKey](arkts-arkui-systemenvkey-c.md)&lt;T&gt; \| [SystemProperties](arkts-arkui-systemproperties-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PropertyDecorator](../../apis-na/arkts-apis/arkts-na-propertydecorator-t.md) |
