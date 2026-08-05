# Env

## Env

```TypeScript
declare function Env<T>(key: SystemEnvKey<T> | SystemProperties): PropertyDecorator
```

Defining Env PropertyDecorator. On API 26.0.0 and above, the parameter also supports the SystemEnvKey\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ type.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-unnamed-declare function Env<T>(key: SystemEnvKey<T> | SystemProperties): PropertyDecorator--><!--Device-unnamed-declare function Env<T>(key: SystemEnvKey<T> | SystemProperties): PropertyDecorator-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; \| SystemProperties | Yes | key value input by the user.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Env decorator |

