# CustomEnvKey

自定义环境变量的Key的类型。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare class CustomEnvKey<S>--><!--Device-unnamed-declare class CustomEnvKey<S>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
protected constructor()
```

用于创建该类的实例对象。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CustomEnvKey-protected constructor()--><!--Device-CustomEnvKey-protected constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## create

```TypeScript
static create<T>(): CustomEnvKey<T>
```

创建一个自定义环境变量Key，作为\@CustomEnv装饰器的参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CustomEnvKey-static create<T>(): CustomEnvKey<T>--><!--Device-CustomEnvKey-static create<T>(): CustomEnvKey<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [CustomEnvKey](arkts-arkui-customenvkey-c.md)&lt;T&gt; | 自定义环境变量Key，用于标识要获取的自定义环境变量。 |

## type

```TypeScript
private type?: S
```

自定义环境变量Key的类型。

**Type:** S

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CustomEnvKey-private type?: S--><!--Device-CustomEnvKey-private type?: S-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

