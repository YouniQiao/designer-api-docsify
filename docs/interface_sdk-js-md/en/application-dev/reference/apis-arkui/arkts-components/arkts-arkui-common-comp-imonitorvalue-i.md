# IMonitorValue

```TypeScript
declare interface IMonitorValue<T>
```

Provides the specific information about the state variable changes monitored by **\@Monitor**, obtained through the **value** API of **IMonitor**. **T** is the state variable type.

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## before

```TypeScript
before: T
```

Value of the state variable before the change.

**Type:** T

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## now

```TypeScript
now: T
```

Current value of the state variable.

**Type:** T

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
path: string
```

Path of the state variable.

**Type:** string

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
