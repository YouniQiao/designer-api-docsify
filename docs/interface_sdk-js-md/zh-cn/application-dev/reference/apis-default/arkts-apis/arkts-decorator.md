# decorator

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [CustomEnvKey](arkts-decorator-customenvkey-c.md) | 自定义环境变量的Key的类型。 |
| [ReadonlyEnvKey](arkts-decorator-readonlyenvkey-c.md) | 只读系统环境变量Key类，用于@Env装饰器的字符串参数格式`'ReadonlyEnvKey.&lt;keyName&gt;'`中的key声明。 |
| [ReadonlySystemEnvKey](arkts-decorator-readonlysystemenvkey-c.md) | 只读系统环境变量Key，继承自[SystemEnvKey](arkts-decorator-systemenvkey-c.md)。 |
| [SystemEnvKey](arkts-decorator-systemenvkey-c.md) | 系统环境变量Key的基类。 |
| [WritableEnvKey](arkts-decorator-writableenvkey-c.md) | 可写系统环境变量Key类，用于@Env装饰器的字符串参数格式`'WritableEnvKey.&lt;keyName&gt;'`中的key声明。 |
| [WritableSystemEnvKey](arkts-decorator-writablesystemenvkey-c.md) | 可写系统环境变量Key，继承自[SystemEnvKey](arkts-decorator-systemenvkey-c.md)。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [ConsumeOptions](arkts-decorator-consumeoptions-i.md) | ConsumeOptions类 |
| [EnvOptions](arkts-decorator-envoptions-i.md) | Env创建可选参数 |
| [IComputedDecoratedVariable](arkts-decorator-icomputeddecoratedvariable-i.md) | 定义@Computed状态变量的接口 |
| [IConsumeDecoratedVariable](arkts-decorator-iconsumedecoratedvariable-i.md) | Define Consume decoration variable interface. |
| [IConsumerDecoratedVariable](arkts-decorator-iconsumerdecoratedvariable-i.md) | Consumer装饰的变量。 |
| [ICustomEnvDecoratedVariable](arkts-decorator-icustomenvdecoratedvariable-i.md) | 定义CustomEnv装饰变量接口。 |
| [IDecoratedImmutableVariable](arkts-decorator-idecoratedimmutablevariable-i.md) | 定义只读状态变量接口 |
| [IDecoratedMutableVariable](arkts-decorator-idecoratedmutablevariable-i.md) | 定义可读写状态变量接口 |
| [IDecoratedReadableVariable](arkts-decorator-idecoratedreadablevariable-i.md) | 定义状态变量接口 |
| [IDecoratedUpdatableVariable](arkts-decorator-idecoratedupdatablevariable-i.md) | Define decorated updatable variable interface. |
| [IDecoratedV1Variable](arkts-decorator-idecoratedv1variable-i.md) | Define V1 decorated variable interface. |
| [IDecoratedV2Variable](arkts-decorator-idecoratedv2variable-i.md) | V2装饰的变量。 |
| [IDecoratedVariable](arkts-decorator-idecoratedvariable-i.md) | 定义状态变量接口 |
| [IEnvDecoratedVariable](arkts-decorator-ienvdecoratedvariable-i.md) | Define Env decoration variable interface. |
| [IGlobalReusePoolVariable](arkts-decorator-iglobalreusepoolvariable-i.md) | 全局复用池句柄。 |
| [ILinkDecoratedVariable](arkts-decorator-ilinkdecoratedvariable-i.md) | Define Link decoration variable interface. |
| [ILocalDecoratedVariable](arkts-decorator-ilocaldecoratedvariable-i.md) | Local装饰的变量。 |
| [ILocalStorageLinkDecoratedVariable](arkts-decorator-ilocalstoragelinkdecoratedvariable-i.md) | Define LocalStorageLink decoration variable interface. |
| [ILocalStoragePropRefDecoratedVariable](arkts-decorator-ilocalstorageproprefdecoratedvariable-i.md) | Define LocalStoragePropRef decoration variable interface. |
| [IMonitor](arkts-decorator-imonitor-i.md) | 当监听的变量变化时，状态管理框架侧将回调开发者注册的函数，并传入变化信息。变化信息的类型即为IMonitor类型。 |
| [IMonitorDecoratedVariable](arkts-decorator-imonitordecoratedvariable-i.md) | Defines @Monitor decorated variable interface. |
| [IMonitorPathInfo](arkts-decorator-imonitorpathinfo-i.md) | Defines Monitor path with its accessor interface. |
| [IMonitorValue](arkts-decorator-imonitorvalue-i.md) |  |
| [IMutableKeyedStateMeta](arkts-decorator-imutablekeyedstatemeta-i.md) | Define mutable state meta interface with key. |
| [IMutableStateMeta](arkts-decorator-imutablestatemeta-i.md) | Define mutable state meta interface. |
| [IObjectLinkDecoratedVariable](arkts-decorator-iobjectlinkdecoratedvariable-i.md) | Define ObjectLink decoration variable interface. |
| [IObserve](arkts-decorator-iobserve-i.md) | Define IObserve interface. |
| [IObservedAnyProp](arkts-decorator-iobservedanyprop-i.md) | 定义IObservableAnyProp类型。 |
| [IObservedObject](arkts-decorator-iobservedobject-i.md) | Define IObservedObject interface. |
| [IParamDecoratedVariable](arkts-decorator-iparamdecoratedvariable-i.md) | Param装饰的变量。 |
| [IParamOnceDecoratedVariable](arkts-decorator-iparamoncedecoratedvariable-i.md) | Param和Once装饰的变量。 |
| [IPropRefDecoratedVariable](arkts-decorator-iproprefdecoratedvariable-i.md) | Define PropRef decoration variable interface. |
| [IProvideDecoratedVariable](arkts-decorator-iprovidedecoratedvariable-i.md) | Define Provide decoration variable interface. |
| [IProviderDecoratedVariable](arkts-decorator-iproviderdecoratedvariable-i.md) | Provider装饰的变量。 |
| [IStateDecoratedVariable](arkts-decorator-istatedecoratedvariable-i.md) | Define state decoration variable interface. |
| [IStateMgmtFactory](arkts-decorator-istatemgmtfactory-i.md) | Define IStateMgmtFactory interface. |
| [IStorageLinkDecoratedVariable](arkts-decorator-istoragelinkdecoratedvariable-i.md) | Define StorageLink decoration variable interface. |
| [IStoragePropRefDecoratedVariable](arkts-decorator-istorageproprefdecoratedvariable-i.md) | Define StoragePropRef decoration variable interface. |
| [ISubscribedWatches](arkts-decorator-isubscribedwatches-i.md) | Define ISubscribedWatches interface. |
| [IVariableOwner](arkts-decorator-ivariableowner-i.md) | 定义一个提供变量相关功能的自定义组件API。 |
| [IWatchSubscriberRegister](arkts-decorator-iwatchsubscriberregister-i.md) | Define IWatchSubscriberRegister interface. |
| [MakeMonitorOptions](arkts-decorator-makemonitoroptions-i.md) | 定义makeMonitor可选配置 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [ComputedCallback](arkts-computedcallback-t.md) | Defines computed callback funciton |
| [LinkSourceType](arkts-linksourcetype-t.md) | Define Link source type. |
| [MonitorCallback](arkts-monitorcallback-t.md) | 触发监听时被调用的回调函数。 |
| [MonitorValueCallback](arkts-monitorvaluecallback-t.md) | 监听状态变量的回调类型。 |
| [RenderIdType](arkts-renderidtype-t.md) | Define int alias. |
| [WatchFuncType](arkts-watchfunctype-t.md) | Defines the callback that is called when state variable is change |
| [WatchIdType](arkts-watchidtype-t.md) | Define int alias. |

