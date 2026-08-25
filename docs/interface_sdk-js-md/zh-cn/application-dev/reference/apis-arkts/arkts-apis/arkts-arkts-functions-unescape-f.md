# unescape

## 导入模块

```TypeScript
```

## unescape

```TypeScript
export function unescape(str: string): string
```

该特性已不再推荐使用。尽管某些 浏览器仍可能支持它，但它可能已从 相关Web标准中移除、正在被 废弃，或仅为兼容性目的而保留。请避免 使用它，并在可能的情况下更新现有代码；请参阅 本页底部的兼容性表格以辅助您做出 决策。请注意，该特性可能随时失效。 unescape()是由浏览器实现的非标准函数， 仅为跨引擎兼容性而被标准化。并非所有 JavaScript引擎都必须实现该函数，因此它可能无法 在所有环境中工作。如有可能，请改用decodeURIComponent()或decodeURI() 替代。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |
