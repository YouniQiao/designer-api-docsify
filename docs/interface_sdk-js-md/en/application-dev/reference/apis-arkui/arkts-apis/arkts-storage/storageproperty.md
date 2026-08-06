# storage/storageProperty

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [AbstractProperty](storageproperty-abstractproperty-i.md) | Define AbstractProperty\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ interface.  AbstractProperty can be understood as a handler or an alias to a property inside LocalStorage / AppStorage singleton allows to read the value with @see get and to change the value with @see set. |
| [SubscribedAbstractProperty](storageproperty-subscribedabstractproperty-i.md) | SubscribedAbstractProperty\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is the return value of  - AppStorage static functions Link(), Prop(), SetAndLink(), and SetAndProp()  - LocalStorage member methods link(), prop(), setAndLink(), and setAndProp()  'T' can be boolean, string, number or custom class.Main functions see get() reads the linked AppStorage/LocalStorage property value,see set(newValue) write a new value to the synched AppStorage/LocalStorage property see aboutToBeDeleted() ends the sync relationship with the AppStorage/LocalStorage property The app must call this function before the SubscribedAbstractProperty\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ object goes out of scope. |

### Enums

| Name | Description |
| --- | --- |
| [ColorMode](storageproperty-colormode-e.md) | Defines the ColorMode of device. |
| [LayoutDirection](storageproperty-layoutdirection-e.md) | Defines the LayoutDirection of device. |

### Types

| Name | Description |
| --- | --- |
| [OnChangeType](arkts-arkui-onchangetype-t.md) | Defines the callback that is called when state variable with value is change |

