# PathPreference

```TypeScript
export type PathPreference = 'auto' | 'primaryCellular' | 'secondaryCellular'
```

HTTP请求指定特定网络的类型枚举。

> **说明：**&gt;
> 推荐在网络并发等场景下使用。

> 当指定的网络没有激活时，系统按照指定默认网络处理。

**起始版本：** 23

**系统能力：** SystemCapability.Communication.NetStack

| 类型 |
| --- |
| 'auto' |
| 'primaryCellular' |
| 'secondaryCellular' |
