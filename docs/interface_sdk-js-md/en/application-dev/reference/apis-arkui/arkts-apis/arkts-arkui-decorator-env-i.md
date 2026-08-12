# Env

Defining Env PropertyDecorator.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export declare @interface Env--><!--Device-unnamed-export declare @interface Env-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value:  string
```

Key value input by the user.On API 26.0.0 and above, it can also support a string literal in the format "ReadonlyEnvKey.&lt;keyName&gt;" or "WritableEnvKey.&lt;keyName&gt;".The key name must be one declared in [ReadonlyEnvKey](arkts-arkui-decorator-readonlyenvkey-c.md#ReadonlyEnvKey) or  
[WritableEnvKey](arkts-arkui-decorator-writableenvkey-c.md#WritableEnvKey). Arbitrary strings are not supported.

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Env-value:  string--><!--Device-Env-value:  string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

