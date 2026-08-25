# configure

## 导入模块

```TypeScript
```

## configure

```TypeScript
function configure(config: ConfigOption): boolean
```

应用事件打点配置方法，可用于配置打点开关、文件目录存储限额大小等功能。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [configure](arkts-performanceanalysis-hiappevent-configure-f.md)

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [ConfigOption](arkts-performanceanalysis-hiappevent-configoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
// 配置应用事件打点功能开关
let config1: hiAppEvent.ConfigOption = {
  disable: true,
};
hiAppEvent.configure(config1);

// 配置事件文件目录存储限额大小
let config2: hiAppEvent.ConfigOption = {
  maxStorage: '100MB',
};
hiAppEvent.configure(config2);
```
