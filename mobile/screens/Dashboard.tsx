import * as React from 'react';
import { StyleSheet, Dimensions } from 'react-native';
import { Text, View } from '../components/Themed';
import Container from '../components/Container';
import ScreenTitle from '../components/ScreenTitle'
import { LineChart } from "react-native-chart-kit";


export default function Dashboard() {
  return (
    <Container>
      <ScreenTitle>Dashboard</ScreenTitle>
      <LineChart
        data={{
          labels: ["January", "February", "March", "April", "May", "June"],
          datasets: [
            {
              data: [
                Math.random() * 100,
                Math.random() * 100,
                Math.random() * 100,
                Math.random() * 100,
                Math.random() * 100,
                Math.random() * 100
              ]
            }
          ]
        }}
        width={Dimensions.get("window").width*0.9} // from react-native
        height={220}
        yAxisLabel="$"
        yAxisSuffix="k"
        yAxisInterval={1} // optional, defaults to 1
        chartConfig={{
          backgroundColor: "#4facfe",
          backgroundGradientFrom: "#4facfe",
          backgroundGradientTo: "#00f2fe",
          decimalPlaces: 2, // optional, defaults to 2dp
          color: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
          labelColor: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
          style: {
            borderRadius: 16
          },
          propsForDots: {
            r: "6",
            strokeWidth: "2",
            stroke: "#4facfe"
          }
        }}
        bezier
        style={{
          marginVertical: 8,
          borderRadius: 16
        }}
      />
    </Container>
  );
}

const styles = StyleSheet.create({
  
});
