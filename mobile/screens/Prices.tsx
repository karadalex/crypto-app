import * as React from 'react';
import { StyleSheet } from 'react-native';
import { Text, View } from '../components/Themed';


export default function Prices() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Prices</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginHorizontal: 20,
    marginTop: 50,
    backgroundColor: "transparent"
  },
  title: {
    fontSize: 35,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});
