# decorator

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [CustomEnvKey](arkts-arkui-decorator-customenvkey-c.md) | 自定义环境变量的Key的类型。 |
| [ReadonlyEnvKey](arkts-arkui-decorator-readonlyenvkey-c.md) | 只读系统环境变量Key类，用于@Env装饰器的字符串参数格式`'ReadonlyEnvKey.&lt;keyName&gt;'`中的key声明。 |
| [ReadonlySystemEnvKey](arkts-arkui-decorator-readonlysystemenvkey-c.md) | 只读系统环境变量Key，继承自[SystemEnvKey](../arkts-components/arkts-arkui-systemenvkey-c.md/arkts-arkui-systemenvkey-c.md)。 |
| [SystemEnvKey](arkts-arkui-decorator-systemenvkey-c.md) | 系统环境变量Key的基类。 |
| [WritableEnvKey](arkts-arkui-decorator-writableenvkey-c.md) | 可写系统环境变量Key类，用于@Env装饰器的字符串参数格式`'WritableEnvKey.&lt;keyName&gt;'`中的key声明。 |
| [WritableSystemEnvKey](arkts-arkui-decorator-writablesystemenvkey-c.md) | 可写系统环境变量Key，继承自[SystemEnvKey](../arkts-components/arkts-arkui-systemenvkey-c.md/arkts-arkui-systemenvkey-c.md)。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [ComponentActive](arkts-arkui-decorator-componentactive-i.md) | 定义ComponentActive方法装饰器。 |
| [ComponentAppear](arkts-arkui-decorator-componentappear-i.md) | 定义ComponentAppear方法装饰器。 |
| [ComponentBuilt](arkts-arkui-decorator-componentbuilt-i.md) | 定义ComponentBuilt方法装饰器 |
| [ComponentDisappear](arkts-arkui-decorator-componentdisappear-i.md) | 定义ComponentDisappear方法装饰器。 |
| [ComponentInactive](arkts-arkui-decorator-componentinactive-i.md) | 定义组件非活动方法装饰器。 |
| [ComponentInit](arkts-arkui-decorator-componentinit-i.md) | 定义ComponentInit方法装饰器。 |
| [ComponentRecycle](arkts-arkui-decorator-componentrecycle-i.md) | 定义ComponentRecycle方法装饰器 |
| [ComponentReuse](arkts-arkui-decorator-componentreuse-i.md) | 定义ComponentReuse方法装饰器。 |
| [Computed](arkts-arkui-decorator-computed-i.md) |  |
| [Consume](arkts-arkui-decorator-consume-i.md) | Defining Consume annotation Consume is used to access the provided state variable for a descendent component |
| [ConsumeOptions](arkts-arkui-decorator-consumeoptions-i.md) | ConsumeOptions类 |
| [Consumer](arkts-arkui-decorator-consumer-i.md) | Defining Consumer annotation Consumer is used to access the provided state variable for a descendent component |
| [CustomEnv](arkts-arkui-decorator-customenv-i.md) | Defining CustomEnv PropertyDecorator. |
| [Env](arkts-arkui-decorator-env-i.md) | Defining Env PropertyDecorator. |
| [EnvOptions](arkts-arkui-decorator-envoptions-i.md) | Env创建可选参数 |
| [Event](arkts-arkui-decorator-event-i.md) |  |
| [IComputedDecoratedVariable](arkts-arkui-decorator-icomputeddecoratedvariable-i.md) | 定义@Computed状态变量的接口 |
| [IConsumeDecoratedVariable](arkts-arkui-decorator-iconsumedecoratedvariable-i.md) | Define Consume decoration variable interface. |
| [IConsumerDecoratedVariable](arkts-arkui-decorator-iconsumerdecoratedvariable-i.md) | Consumer装饰的变量。 |
| [ICustomEnvDecoratedVariable](arkts-arkui-decorator-icustomenvdecoratedvariable-i.md) | 定义CustomEnv装饰变量接口。 |
| [IDecoratedImmutableVariable](arkts-arkui-decorator-idecoratedimmutablevariable-i.md) | 定义只读状态变量接口 |
| [IDecoratedMutableVariable](arkts-arkui-decorator-idecoratedmutablevariable-i.md) | 定义可读写状态变量接口 |
| [IDecoratedReadableVariable](arkts-arkui-decorator-idecoratedreadablevariable-i.md) | 定义状态变量接口 |
| [IDecoratedUpdatableVariable](arkts-arkui-decorator-idecoratedupdatablevariable-i.md) | Define decorated updatable variable interface. |
| [IDecoratedV1Variable](arkts-arkui-decorator-idecoratedv1variable-i.md) | Define V1 decorated variable interface. |
| [IDecoratedV2Variable](arkts-arkui-decorator-idecoratedv2variable-i.md) | V2装饰的变量。 |
| [IDecoratedVariable](arkts-arkui-decorator-idecoratedvariable-i.md) | 定义状态变量接口 |
| [IEnvDecoratedVariable](arkts-arkui-decorator-ienvdecoratedvariable-i.md) | Define Env decoration variable interface. |
| [IGlobalReusePoolVariable](arkts-arkui-decorator-iglobalreusepoolvariable-i.md) | 全局复用池句柄。 |
| [ILinkDecoratedVariable](arkts-arkui-decorator-ilinkdecoratedvariable-i.md) | Define Link decoration variable interface. |
| [ILocalDecoratedVariable](arkts-arkui-decorator-ilocaldecoratedvariable-i.md) | Local装饰的变量。 |
| [ILocalStorageLinkDecoratedVariable](arkts-arkui-decorator-ilocalstoragelinkdecoratedvariable-i.md) | Define LocalStorageLink decoration variable interface. |
| [ILocalStoragePropRefDecoratedVariable](arkts-arkui-decorator-ilocalstorageproprefdecoratedvariable-i.md) | Define LocalStoragePropRef decoration variable interface. |
| [IMonitor](arkts-arkui-decorator-imonitor-i.md) | 当监听的变量变化时，状态管理框架侧将回调开发者注册的函数，并传入变化信息。变化信息的类型即为IMonitor类型。 |
| [IMonitorDecoratedVariable](arkts-arkui-decorator-imonitordecoratedvariable-i.md) | Defines @Monitor decorated variable interface. |
| [IMonitorPathInfo](arkts-arkui-decorator-imonitorpathinfo-i.md) | Defines Monitor path with its accessor interface. |
| [IMonitorValue](arkts-arkui-decorator-imonitorvalue-i.md) |  |
| [IMutableKeyedStateMeta](arkts-arkui-decorator-imutablekeyedstatemeta-i.md) | Define mutable state meta interface with key. |
| [IMutableStateMeta](arkts-arkui-decorator-imutablestatemeta-i.md) | Define mutable state meta interface. |
| [IObjectLinkDecoratedVariable](arkts-arkui-decorator-iobjectlinkdecoratedvariable-i.md) | Define ObjectLink decoration variable interface. |
| [IObserve](arkts-arkui-decorator-iobserve-i.md) | Define IObserve interface. |
| [IObservedAnyProp](arkts-arkui-decorator-iobservedanyprop-i.md) | 定义IObservableAnyProp类型。 |
| [IObservedObject](arkts-arkui-decorator-iobservedobject-i.md) | Define IObservedObject interface. |
| [IParamDecoratedVariable](arkts-arkui-decorator-iparamdecoratedvariable-i.md) | Param装饰的变量。 |
| [IParamOnceDecoratedVariable](arkts-arkui-decorator-iparamoncedecoratedvariable-i.md) | Param和Once装饰的变量。 |
| [IPropRefDecoratedVariable](arkts-arkui-decorator-iproprefdecoratedvariable-i.md) | Define PropRef decoration variable interface. |
| [IProvideDecoratedVariable](arkts-arkui-decorator-iprovidedecoratedvariable-i.md) | Define Provide decoration variable interface. |
| [IProviderDecoratedVariable](arkts-arkui-decorator-iproviderdecoratedvariable-i.md) | Provider装饰的变量。 |
| [IStateDecoratedVariable](arkts-arkui-decorator-istatedecoratedvariable-i.md) | Define state decoration variable interface. |
| [IStateMgmtFactory](arkts-arkui-decorator-istatemgmtfactory-i.md) | Define IStateMgmtFactory interface. |
| [IStorageLinkDecoratedVariable](arkts-arkui-decorator-istoragelinkdecoratedvariable-i.md) | Define StorageLink decoration variable interface. |
| [IStoragePropRefDecoratedVariable](arkts-arkui-decorator-istorageproprefdecoratedvariable-i.md) | Define StoragePropRef decoration variable interface. |
| [ISubscribedWatches](arkts-arkui-decorator-isubscribedwatches-i.md) | Define ISubscribedWatches interface. |
| [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | 定义一个提供变量相关功能的自定义组件API。 |
| [IWatchSubscriberRegister](arkts-arkui-decorator-iwatchsubscriberregister-i.md) | Define IWatchSubscriberRegister interface. |
| [Link](arkts-arkui-decorator-link-i.md) |  |
| [Local](arkts-arkui-decorator-local-i.md) |  |
| [LocalStorageLink](arkts-arkui-decorator-localstoragelink-i.md) | Defining LocalStorageLink annotation LocalStorageLink is used to create a two-way data synchronization with the attribute in LocalStorage. |
| [LocalStoragePropRef](arkts-arkui-decorator-localstoragepropref-i.md) | Defining LocalStoragePropRef annotation LocalStoragePropRef is an annotation which is mutable.Any object property modifications made through LocalStoragePropRef are visible in the LocalStorage, which is different from LocalStorageProp.In order to prevent this, need to take a deep copy of LocalStorage data. |
| [MakeMonitorOptions](arkts-arkui-decorator-makemonitoroptions-i.md) | 定义makeMonitor可选配置 |
| [Monitor](arkts-arkui-decorator-monitor-i.md) | Defining Monitor annotation Monitor provides the capability of listening for state variables of V2. |
| [ObjectLink](arkts-arkui-decorator-objectlink-i.md) |  |
| [Observed](arkts-arkui-decorator-observed-i.md) |  |
| [ObservedV2](arkts-arkui-decorator-observedv2-i.md) |  |
| [Once](arkts-arkui-decorator-once-i.md) |  |
| [Param](arkts-arkui-decorator-param-i.md) |  |
| [PropRef](arkts-arkui-decorator-propref-i.md) |  |
| [Provide](arkts-arkui-decorator-provide-i.md) | Defining Provide annotation Provide is used for two-way data synchronization with descendant components when state data needs to be transferred between multiple levels. An @Provide decorated state variable exists in the ancestor component and is said to be "provided" to descendent components. |
| [Provider](arkts-arkui-decorator-provider-i.md) | Defining Provider annotation Provider is used for two-way data synchronization with descendant components when state data needs to be transferred between multiple levels. An @Provider decorated state variable exists in the ancestor component and is said to be "provider" to descendent components. |
| [Require](arkts-arkui-decorator-require-i.md) |  |
| [State](arkts-arkui-decorator-state-i.md) |  |
| [StorageLink](arkts-arkui-decorator-storagelink-i.md) | Defining StorageLink annotation StorageLink is used to create a two-way data synchronization between the variable it decorates and the attribute with the given key in AppStorage. |
| [StoragePropRef](arkts-arkui-decorator-storagepropref-i.md) | Defining StoragePropRef annotation StoragePropRef is an annotation which is mutable.Any object property modifications made through StoragePropRef are visible in the AppStorage, which is different from StorageProp.In order to prevent this, need to take a deep copy of AppStorage instance data. |
| [SyncMonitor](arkts-arkui-decorator-syncmonitor-i.md) | Define SyncMonitor MethodDecorator. Decorator path parameters are the same as defined for Monitor.The function decorator is functionally equivalent to the UIUtils.addMonitor API with isSynchronous enabled.SyncMonitor must contain at least one path item, with multiple path items separated by commas.Path items are either observed attribute names or array item indices.The path in SyncMonitor supports wildcard at the end of a path item, but path items must never appear at the beginning or in the middle of a path. All other paths using one or more wildcard are invalid. |
| [Trace](arkts-arkui-decorator-trace-i.md) |  |
| [Track](arkts-arkui-decorator-track-i.md) |  |
| [Watch](arkts-arkui-decorator-watch-i.md) | Defining Watch annotation Watch is used to listen for state variables. |

### 类型

| 名称 | 说明 |
| --- | --- |
| [ComputedCallback](arkts-arkui-computedcallback-t.md) | Defines computed callback funciton |
| [LinkSourceType](arkts-arkui-linksourcetype-t.md) | Define Link source type. |
| [MonitorCallback](arkts-arkui-monitorcallback-t.md) | 触发监听时被调用的回调函数。 |
| [MonitorValueCallback](arkts-arkui-monitorvaluecallback-t.md) | 监听状态变量的回调类型。 |
| [RenderIdType](arkts-arkui-renderidtype-t.md) | Define int alias. |
| [WatchFuncType](arkts-arkui-watchfunctype-t.md) | Defines the callback that is called when state variable is change |
| [WatchIdType](arkts-arkui-watchidtype-t.md) | Define int alias. |

