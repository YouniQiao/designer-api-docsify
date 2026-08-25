# ParallelizeUI

## 导入模块

```TypeScript
```

## ParallelizeUI

```TypeScript
export declare function ParallelizeUI(
  options: ParallelOption | undefined,
  content_: CustomBuilder,
): void
```

声明式的并行化创建UI方法。options参数为undefined时，默认开启并行化创建。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ParallelOption](arkts-arkui-arkui-parallelize-paralleloption-i.md) \| undefined | 是 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |


## ParallelizeUI

```TypeScript
export declare function ParallelizeUI<T>(
  options: ParallelOption | undefined,
  param: () => T,
  content_: CustomBuilderT<T>,
): void
```

声明式UI并行化创建接口。该方法支持在并行化环境中安全地使用外部定义的状态变量。options参数为undefined时，默认开启并行化创建。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ParallelOption](arkts-arkui-arkui-parallelize-paralleloption-i.md) \| undefined | 是 |
| param | () = & gt; T | 是 |
| content_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;T&gt; | 是 |


## ParallelizeUI

```TypeScript
export declare function ParallelizeUI<V, T>(
  options: ParallelOption | undefined,
  arr: Array<V>,
  param: (item: V, index: int) => T,
  content_: CustomBuilderT<T>
): void
```

声明式UI并行化循环创建接口。在非List和Grid中使用时，并行创建数组中定义的所有UI节点。在List或Grid容器中使用时，仅按需并行创建当前可见的节点。options参数为undefined时，默认开启并行化创建。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ParallelOption](arkts-arkui-arkui-parallelize-paralleloption-i.md) \| undefined | 是 |
| arr | Array & lt;V & gt; | 是 |
| param | (item: V, index: int) = & gt; T | 是 |
| content_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;T&gt; | 是 |
