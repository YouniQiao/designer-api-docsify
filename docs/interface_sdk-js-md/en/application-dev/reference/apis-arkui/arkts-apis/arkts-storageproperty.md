# storageProperty

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [AbstractProperty](arkts-arkui-storageproperty-abstractproperty-i.md) | Define AbstractProperty&lt;T&gt; interface. AbstractProperty can be understood as a handler or an alias to a property inside LocalStorage / AppStorage singleton allows to read the value with @see get and to change the value with @see set. |
| [SubscribedAbstractProperty](arkts-arkui-storageproperty-subscribedabstractproperty-i.md) | SubscribedAbstractProperty&lt;T&gt; is the return value of - AppStorage static functions Link(), Prop(), SetAndLink(), and SetAndProp() - LocalStorage member methods link(), prop(), setAndLink(), and setAndProp() 'T' can be boolean, string, number or custom class. Main functions see get() reads the linked AppStorage/LocalStorage property value, see set(newValue) write a new value to the synched AppStorage/LocalStorage property see aboutToBeDeleted() ends the sync relationship with the AppStorage/LocalStorage property The app must call this function before the SubscribedAbstractProperty&lt;T&gt; object goes out of scope. |

### Enums

| Name | Description |
| --- | --- |
| [ColorMode](arkts-arkui-storageproperty-colormode-e.md) | Defines the ColorMode of device. |
| [LayoutDirection](arkts-arkui-storageproperty-layoutdirection-e.md) | Defines the LayoutDirection of device. |

### Types

| Name | Description |
| --- | --- |
| [OnChangeType](arkts-arkui-onchangetype-t.md) | Defines the callback that is called when state variable with value is change |

