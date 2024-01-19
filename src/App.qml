import QtQuick
import QtQuick.Controls

ApplicationWindow {
    id: root
    title: '<windowTitle>'
    visible: true
    width: Screen.width * 0.8
    height: Screen.height * 0.8

    Component.onCompleted: {
        console.log('Application window completed');
    }
}
