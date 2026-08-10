# configure

## configure

```TypeScript
function configure(config: ConfigOption): boolean
```

应用事件打点配置方法，可用于配置打点开关、文件目录存储限额大小等功能。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.hiviewdfx.hiAppEvent/hiAppEvent#configure

<!--Device-hiAppEvent-function configure(config: ConfigOption): boolean--><!--Device-hiAppEvent-function configure(config: ConfigOption): boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [ConfigOption](arkts-performanceanalysis-hiappevent-configoption-i.md) | Yes | 应用事件打点配置项对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 配置结果，true 表示配置成功，false 表示配置失败。 |

## Examples

```TypeScript
// Set the application event logging switch.
let config1: hiAppEvent.ConfigOption = {
  disable: true,
};
hiAppEvent.configure(config1);

// Configure the maximum size of the directory that stores the event logging files.
let config2: hiAppEvent.ConfigOption = {
  maxStorage: '100M',
};
hiAppEvent.configure(config2);
```

