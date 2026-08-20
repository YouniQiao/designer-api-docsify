# Environment

Defines the Environment interface.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class Environment--><!--Device-unnamed-export declare class Environment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## envProp

```TypeScript
static envProp<T>(key: string, value: T): boolean
```

Creates a new property in AppStorage. The UI framework implementation takes care of updating its value whenever the named device environment property changes. Recommended use is at app startup. The function call fails and returns false if a property with given name exists in AppStorage already. It is wrong API use to access a property with given name in AppStorage before calling Environment.envProp.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Environment-static envProp<T>(key: string, value: T): boolean--><!--Device-Environment-static envProp<T>(key: string, value: T): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | environment property |
| value | T | Yes | is the default value if cannot get the environment property value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | false if method failed |

## envProps

```TypeScript
static envProps(props: EnvPropsOptions[]): void
```

Called when multiple property values are added to Environment.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Environment-static envProps(props: EnvPropsOptions[]): void--><!--Device-Environment-static envProps(props: EnvPropsOptions[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| props | [EnvPropsOptions](arkts-arkui-environment-envpropsoptions-i.md)[] | Yes | environment parameter |

## keys

```TypeScript
static keys(): Array<string>
```

returns an array of all environment property keys

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Environment-static keys(): Array<string>--><!--Device-Environment-static keys(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | all environment property keys |

