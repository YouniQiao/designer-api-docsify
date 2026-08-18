# WithEnvAttribute(Define the WithEnv component that allows setting environment properties for child components.)

Define the WithEnv attribute functions.

**Since:** 26.0.0

<!--Device-unnamed-export declare class WithEnvAttribute--><!--Device-unnamed-export declare class WithEnvAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## customEnv

```TypeScript
customEnv<T>(key: CustomEnvKey<T>,  value: T): WithEnvAttribute
```

Defining Custom Environment Variables

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WithEnvAttribute-customEnv<T>(key: CustomEnvKey<T>,  value: T): WithEnvAttribute--><!--Device-WithEnvAttribute-customEnv<T>(key: CustomEnvKey<T>,  value: T): WithEnvAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [CustomEnvKey](../arkts-components/arkts-arkui-customenvkey-c.md)&lt;T&gt; | Yes |
| value | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WithEnvAttribute](arkts-arkui-arkui-withenv-withenvattribute-c.md) |

## env

```TypeScript
env<T>(key: WritableSystemEnvKey<T>, value: T): WithEnvAttribute
```

Defining System Environment Variables

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WithEnvAttribute-env<T>(key: WritableSystemEnvKey<T>, value: T): WithEnvAttribute--><!--Device-WithEnvAttribute-env<T>(key: WritableSystemEnvKey<T>, value: T): WithEnvAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [WritableSystemEnvKey](../arkts-components/arkts-arkui-writablesystemenvkey-c.md)&lt;T&gt; | Yes |
| value | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WithEnvAttribute](arkts-arkui-arkui-withenv-withenvattribute-c.md) |
