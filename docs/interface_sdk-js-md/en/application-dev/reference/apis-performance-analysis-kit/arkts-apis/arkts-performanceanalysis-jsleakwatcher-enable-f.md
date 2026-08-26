# enable

## Modules to Import

```TypeScript
```

## enable

```TypeScript
function enable(isEnable: boolean): void
```

Enables the detection for ArkTS object leaks. This function is disabled by default.

**Since:** 12

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnable | boolean | Yes | Whether to enable **jsLeakWatcher**. **true**: yes; **false**: no. |

**Examples**

```TypeScript
jsLeakWatcher.enable(true);
```
